#!/bin/bash

docker build generate -t python-docker:generate --no-cache

docker run -v $(pwd)/exported-data/:/app/exported-data/ -it python-docker:generate 