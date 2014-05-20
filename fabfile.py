from fabric.api import *
import fabric.contrib.project as project
import os

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

#want a deploy function as well.

