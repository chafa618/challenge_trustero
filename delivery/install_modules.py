#!/usr/bin/env python
# coding: utf-8

from spacy.cli.download import download, link

download(model='en_core_web_lg')
link(origin='en_core_web_lg', link_name='en')

import nltk

nltk.download('punkt')
