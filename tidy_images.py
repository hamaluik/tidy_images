# -*- coding: utf-8 -*-
"""
Tidy Images
=================


"""

from pelican import signals, contents
import re

replacementString = r'''<figure><img src="\1"><figcaption>\2</figcaption></figure>'''

def processImages(content):
	if isinstance(content, contents.Static):
		return
	
	text = re.sub(r"\{image-caption\[(?P<url>.*?)\]\[(?P<caption>.*?)\]\}", replacementString, content._content)
	content._content = text

def register():
	signals.content_object_init.connect(processImages)
