#!/usr/bin/env bash

set -o errexit

python -m gunicorn -c ./gunicorn.conf.py -b "0.0.0.0:${PORT:=8000}"
