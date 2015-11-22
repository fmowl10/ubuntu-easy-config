#!/bin/bash
# Part of ubuntu-easy-config https://github.com/minwook-shin/ubuntu-easy-config
#
# See LICENSE file for copyright and license details
#
# This program written for noob for ubuntu and "Korean Setting" by minwook Shin and fmowl10
# in 21st and 22sc of November 2015




VERSION=0.0.1 #버전
argc=$#       #인자들
argv0=$0
argv1=$1


#인자 처리
argcv()
{
    if [ $argc -gt 0 ];
    then
        if [ "$argv1" == "-h" -o "$argv1" == "--help" ];
        then
            echo -e "사용볍: ./ubuntu-easy-config.sh [옵션]"
            echo -e "옵션:"
            echo -e "\t-h, --help\t도움말을 보여줍니다."
            echo -e "\t-v, --version\t버전 정보를 보여줍니다."
            echo -e "\t-s, --setting\t실행전 세팅을 합니다."
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

#언어 파일 설정
setting(){
	cd lang/
	echo "script start"
	msgfmt -o main_ko.mo main_ko.po
	echo "main/messages_ko.mo created !"
	msgfmt -o main_en.mo main_en.po
	echo "main/messages_en.mo created !"
	msgfmt -o desktop_ko.mo desktop_ko.po
	echo "desktop/messages_ko.mo created !"
	msgfmt -o desktop_en.mo desktop_en.po
	echo "desktop/messages_en.mo created !"
	exit 0
}

#앱실행
runnigapp(){
	cd pages/
	echo "run ubuntu-easy-config."
	python main_page.py
	# echo "You can exit this terminal."
}

#권한체크
checkingroot(){
	if [ $(id -u) -ne 0 ]; then
	        echo 이 스크립트는 루트 권한을 필요로 합니다. sudo ./ubuntu-easy-config.sh 로 실행시켜주십시오.
	        exit 0
        fi
}

#실행문
argcv
checkingroot
runnigapp
