#!/bin/bash
# http://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)#Google_Text_to_Speech

say() { local IFS=+;/usr/bin/mplayer -ao alsa -really-quiet -noconsolecontrols "http://translate.google.com/translate_tts?tl=en&q=$*"; }
say $*