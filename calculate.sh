#!/bin/bash

docker build calculate -t python-docker:calculate --no-cache

docker run -it python-docker:calculate 