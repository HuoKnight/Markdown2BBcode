import re
from bb_sub import *

with open('markdown.txt', 'rb') as mkdwn:
    markdown_string = mkdwn.read().decode()

bbcode = bbify(markdown_string)

with open("bbcode.txt", 'w') as bbcd:
    bbcd.write(bbcode)











# Possibly remove?
# Break markdown into segments and classify each segment.
# `segments` contains data in the following format:
#
# <index>(int): {<classifier>(str): <segment>(str)}
#
# e.g. "# Title Text" would be stored as:
#
# 0: {header_1: 'Title Text'}

# segments = {}
# seg_index = 0
# bbcode_string = ''
# for line in markdown_string.split('\n'):
#     # HEADERS
#     header_tag = re.search("^#.*", line) # Finds all header lines
#     if header_tag:
#         count = header_tag.group(0).count('#') # Number of '#' refers to size of header
        
        
#         # segments[seg_index] = {"header_%d" % count: line.split('\r')[0]}
#     # BOLD
#     bold_tag = re.search("\*\*.*\*\*", line)
#     if bold_tag:
        

    
    