#!/usr/bin/env bash
set -e

pipenv install

pipenv run python ./app.py

