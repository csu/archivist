# Christopher Su
# 07/2016
from __future__ import print_function
from __future__ import unicode_literals
from rtmbot.core import Plugin

import os
import json

archive_dir = os.environ.get('SLACK_ARCHIVIST_OUTPUT_DIR')
if not archive_dir:
    print('The SLACK_ARCHIVIST_OUTPUT_DIR env variable must be set.')
    quit()

if not os.path.exists(archive_dir):
    os.makedirs(archive_dir)

class ArchivistPlugin(Plugin):
    # This implementation is better but idk if rtmbot has a close handler
    # file_handlers = {}
    # def process_message(data):
    #   if data['channel'] not in file_handlers:
    #     file_handlers[data['channel']] = open(os.path.join(data['channel'] + '.txt'))
      
    #   file_handlers[data['channel']].write(data + '\n')

    def process_message(self, data):
        with open(os.path.join(archive_dir, data['channel'] + '.txt'), 'a') as f:
          f.write(json.dumps(data) + '\n')
