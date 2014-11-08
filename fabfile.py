from fabric.api import *
import fabric.contrib.project as project
import os,re

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = '.'
env.content_path = './_content'
DEPLOY_PATH = env.deploy_path

def build():
    local('pelican -s pelicanconf.py -o {deploy_path}  {content_path}'.format(**env))

def clean():
    local('rm -rf {deploy_path}/*.html {deploy_path}/category {deploy_path}/pages {deploy_path}/tag {deploy_path}/author {deploy_path}/theme  '.format(**env))
def serve():
    local('cd {deploy_path} && python -m SimpleHTTPServer'.format(**env))

def rebuild():
    clean()
    build()
    
def reserve():
    build()
    serve()


def deploy():
    os.chdir(DEPLOY_PATH)
    local('git add .')
    local('git commit -am "automated commit"')
    local('git push origin master')



def create_post(notebook_name):
    ipython_file_path=os.path.join('/home/trevor/Notebooks/trvrm',notebook_name +'.ipynb')
    
    assert os.path.isfile(ipython_file_path),ipython_file_path
    metadata_file_path=os.path.abspath(os.path.join(env.content_path,notebook_name+'.meta'))
    
    #assert os.path.isfile(metadata_file_path), metadata_file_path
    
    rst_file_path=os.path.abspath(os.path.join(env.content_path,notebook_name+'.rst'))
    
    #This is a problem
    os.chdir(env.content_path)
    
    command='ipython nbconvert --to rst {0}'.format(ipython_file_path)

    local(command)
    
    meta=file(metadata_file_path).read()
    
    
    rst=file(rst_file_path).read() 
 
    rst=re.compile(r'^\.\.\scode::', re.MULTILINE).sub('.. code-block::',rst)
    
    #replace double back-ticks with :code:`...`
    rst=re.compile(r'``(.*)``',re.MULTILINE).sub(r':code:`\g<1>`',rst)
    
    with file(rst_file_path,'w') as out:
        out.write(meta)
        out.write(rst)
        
    
    print 'done'
    

#want a deploy function as well.

