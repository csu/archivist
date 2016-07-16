# archivist

A Slack bot for managing chat archives.

## Installation
1. Install [python-rtmbot](https://github.com/slackhq/python-rtmbot)
2. Run `git clone https://github.com/csu/archivist.git` in the `plugins` folder
3. Configure rtmbot (see its readme)
4. Set the `SLACK_ARCHIVIST_OUTPUT_DIR` env variable to the desired output directory
4. Run rtmbot

### Example
```bash
git clone https://github.com/slackhq/python-rtmbot.git
cd python-rtmbot
# make virtual env
# enter virtual env
pip install -r requirements.txt

cd plugins
git clone https://github.com/csu/archivist.git
cd ..

cp doc/example-config/rtmbot.conf .
vi rtmbot.conf

export SLACK_ARCHIVIST_OUTPUT_DIR="/home/csu/archivist-data"

./rtmbot.py
```

## Contributing
Pull requests and issues are welcome.

### Maintainers
* [Christopher Su](https://christopher.su) ([csu](https://github.com/csu))
