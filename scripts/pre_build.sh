#!/bin/zsh
echo
echo "Cleaning up .DS_Store files:$(tput bold)$(tput setaf 0)"
find "$1" -type f -name .DS_Store -print -delete
echo
echo "$(tput init)Formatting files:"
organize-imports-cli "$1"/**/*.js
prettier -w "$1"
echo
