from __future__ import unicode_literals
import os
import json

crontable = []
outputs = []

archive_dir = '/Users/christophersu/code/archivist-data'

if not os.path.exists(archive_dir):
  os.makedirs(archive_dir)

# This implementation is better but idk if rtmbot has a close handler
# file_handlers = {}
# def process_message(data):
#   if data['channel'] not in file_handlers:
#     file_handlers[data['channel']] = open(os.path.join(data['channel'] + '.txt'))
  
#   file_handlers[data['channel']].write(data + '\n')

def process_message(data):
  print data
  print os.path.join(archive_dir, data['channel'] + '.txt')
  with open(os.path.join(archive_dir, data['channel'] + '.txt'), 'a') as f:
    f.write(json.dumps(data) + '\n')