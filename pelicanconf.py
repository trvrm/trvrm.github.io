#!/usr/bin/env python
# -*- coding: utf-8 -*- #

'''

    useful: http://mathamy.com/migrating-to-github-pages-using-pelican.html
'''

from __future__ import unicode_literals

AUTHOR = u'trvrm'
SITENAME = u'trvrm'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

PYGMENTS_STYLE = 'tango'
DEFAULT_LANG = u'en'


THEME = "../pelican-bootstrap3"

#THEME = "../pelican-clean-blog"
DISPLAY_PAGES_ON_MENU=True
DISPLAY_CATEGORIES_ON_MENU=True
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

DEFAULT_PAGINATION = 8

DEFAULT_DATE = "fs"


#theme options
BOOTSTRAP_NAVBAR_INVERSE=False
BOOTSTRAP_THEME = 'flatly'
GITHUB_USER='trvrm'
TWITTER_WIDGET_ID='586183094564220928'

PLUGIN_PATHS = ["../pelican-plugins"]
PLUGINS=['twitter_bootstrap_rst_directives']


DISPLAY_ARTICLE_ON_INDEX=True