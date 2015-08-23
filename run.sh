#!/bin/sh
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
cd ../pages/
echo "run ubuntu-config."
python main_page.py
# echo "You can exit this terminal."
