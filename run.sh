#!/bin/sh
echo "script start!"
msgfmt -o lang/main/messages_ko.mo lang/main/messages_ko.po
echo "messages_ko has been translated !"
msgfmt -o lang/main/messages_en.mo lang/main/messages_en.po
echo "messages_en has been translated !"
msgfmt -o lang/desktop/messages_ko.mo lang/desktop/messages_ko.po
echo "messages_ko has been translated !"
msgfmt -o lang/desktop/messages_en.mo lang/desktop/messages_en.po
echo "messages_en has been translated !"
cd pages/
echo "pages folder opend !"
echo "run ubuntu-config !"
python main_page.py
echo "exit ubuntu-config"

exit 0


