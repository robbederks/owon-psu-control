#!/bin/bash -e
rm -r dist/*
python -m build
python -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

