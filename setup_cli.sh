#!/bin/bash

sudo apt-get install -y python3
sudo apt install python3-pip
sudo pip3 install typer

sudo chmod +x fopt
sudo echo 'export FOPT_API_HOST=undefined' >> ~/.bashrc
sudo echo 'export PATH=$HOME/faas-optimizer/cli:$PATH' >> ~/.bashrc


echo '\n\e[32mPlease add the following lines to your .bashrc or your .bash_profile file:\e[0m\n' 
echo '\t\e[34mexport PATH=$HOME/faas-optimizer/cli:$PATH\n\texport FOPT_API_HOST=<FAAS-OPTIMIZER-URI>:<FAAS-OPTIMIZER-PORT>\e[0m\n'
echo '\e[32mThen run:\e[0m\n'
echo '\t\e[31msource $HOME/.bash_profile or source $HOME/.bashrc\e[0m\n\n'

