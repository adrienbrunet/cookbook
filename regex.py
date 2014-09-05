# coding: utf-8

import re

# Aim: retrieve in a list all content between the block tags


text = "lorem ipsum <block>mother fucking content</block>"


pattern = r"<block>(.*?)</block>"
list_block_text = re.findall(
  pattern,
  text,
  flags=re.DOTALL
)
