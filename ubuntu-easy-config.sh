#!/bin/bash
# Part of ubuntu-easy-config https://github.com/minwook-shin/ubuntu-easy-config
#
# See LICENSE file for copyright and license details
#
# This program written for beginner for ubuntu and "ubuntu Setting" by minwook Shin and hedone21, fmowl10
# in 21st and 22sc of November 2015




VERSION=0.1.1 #version
argc=$#
argv0=$0
argv1=$1


#argcv process
argcv()
{
    if [ $argc -gt 0 ];
    then
        if [ "$argv1" == "-h" -o "$argv1" == "--help" ];
        then
            echo -e "How to use: ./ubuntu-easy-config.sh [option]"
            echo -e "option:"
            echo -e "\t-h, --help\t Show Help."
            echo -e "\t-v, --version\t Show version information."
            echo -e "\t-s, --setting\t Before running."
        fi
        if [ "$argv1" == "-v" -o "$argv1" == "--version" ];
        then
            echo $VERSION
        fi
        if [ "$argv1" == "-s" -o "$argv1" == "--setting" ];
        then
            setting
        fi

        exit 0
    fi
}

#Setting the language file
setting(){
	cd lang/
	echo "script start"
	msgfmt -o main_en.mo main_en.po
	echo "main/messages_en.mo created !"
	msgfmt -o desktop_en.mo desktop_en.po
	echo "desktop/messages_en.mo created !"
	exit 0
}

#Launch app
runnigapp(){
	cd pages/
	echo "run ubuntu-easy-config."
	python main_page.py
	# echo "You can exit this terminal."
}

#Check permissions
checkingroot(){
	if [ $(id -u) -ne 0 ]; then
	        echo This script requires root.$sudo ./ubuntu-easy-config.sh
	        exit 0
        fi
}

#running core
argcv
checkingroot
runnigapp
