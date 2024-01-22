#!/bin/sh
echo
echo Copying files:
cp -v "$1"/dist/preview.png "$1"/assets
cp -v "$1"/dist/*.bin ~/Dropbox/.zmake
echo
