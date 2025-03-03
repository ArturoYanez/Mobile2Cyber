#!/bin/zsh
pkg update -y
cat packages.txt | xargs pkg install -y
termux-setup-storage
