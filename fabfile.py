from fabric.api import *
import fabric.contrib.project as project
import os

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = '.'
env.theme_path = '~/pelican-themes/pelican-bootstrap3'
env.content_path = './_content'
DEPLOY_PATH = env.deploy_path

def build():
    local('pelican -s pelicanconf.py -o {deploy_path} -t {theme_path} {content_path}'.format(**env))


def serve():
    local('cd {deploy_path} && python -m SimpleHTTPServer'.format(**env))

def reserve():
    build()
    serve()


def deploy():
    os.chdir(DEPLOY_PATH)
    local('git add .')
    local('git commit -am "Content Changes"')
    local('git push origin master')

#want a deploy function as well.

