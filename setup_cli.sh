#!/bin/bash
set -e
set -x


sudo apt-get install -y python3
sudo apt-get install pip3
sudo pip3 install typer

sudo chmod +x fopt

echo 'export PATH=$HOME/faas-optimizer/cli:$PATH' > "$HOME/.bash_profile"

