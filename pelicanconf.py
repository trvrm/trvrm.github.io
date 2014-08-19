#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'trvrm'
SITENAME = u'trvrm'
SITEURL = ''

TIMEZONE = 'Europe/Paris'
BOOTSTRAP_THEME = 'readable'
PYGMENTS_STYLE = 'tango'
DEFAULT_LANG = u'en'
#THEME = "../pelican-themes/pelican-bootstrap3"
THEME = "../pelican-themes-2/pelican-bootstrap3"
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('IPython','http://ipython.org/'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/trvrm',),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DEFAULT_DATE = "fs"


PLUGIN_PATHS = ['../pelican-plugins']
#enabling the PDF plugin messes up regular pygments output.
PLUGINS = ['ipythonnb']
#PLUGINS = [ 'liquid_tags.notebook']
#NOTEBOOK_DIR = '/home/trevor/Notebooks/code_samples'


#DOCUTILS_SETTINGS={'report_level':'quiet'}
