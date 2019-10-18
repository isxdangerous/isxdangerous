#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Is X Dangerous Editorial Board'
SITENAME = u'Is X Dangerous?'
SITESUBTITLE = 'Cataloging the world’s Dangers'
SITEURL = ''
PATH = 'content'
THEME = './themes/isxdangerous'
OUTPUT_PATH = 'docs/' # for github pages hosting
PLUGIN_PATHS = ['./plugins/']
PLUGINS = ['sitemap']
SITEMAP = { 'format': 'xml', 'exclude': ['tag/', 'tags', 'archive'] }
ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}.html'

TIMEZONE = 'EST'
DATE_FORMATS = {
        'en': '%A, %B %d, %Y'
    }

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

SUMMARY_MAX_LENGTH = 40

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
