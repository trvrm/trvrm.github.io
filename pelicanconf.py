#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'trvrm'
SITENAME = u'trvrm'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

PYGMENTS_STYLE = 'tango'
DEFAULT_LANG = u'en'


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

DEFAULT_DATE = "fs"


#theme options
BOOTSTRAP_NAVBAR_INVERSE=False
BOOTSTRAP_THEME = 'flatly'
GITHUB_USER='trvrm'
TWITTER_WIDGET_ID='586183094564220928'

PLUGIN_PATHS = ["/home/trevor/pelican-plugins"]
PLUGINS=['twitter_bootstrap_rst_directives']
