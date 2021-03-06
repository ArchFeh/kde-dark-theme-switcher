#!/bin/bash
STATUS=$(qdbus org.kde.KWin /ColorCorrect org.kde.kwin.ColorCorrect.nightColorInfo | sed -n '/Active: true/'p)

if [ "$STATUS" = "Active: true" ]; then
	lookandfeeltool --apply com.github.vinceliuice.McMojave
	sed -i 's/Mojave-light/Mojave-dark/g' /home/$(whoami)/.config/gtk-3.0/settings.ini
	sed -i 's/McMojave-light/McMojave/g' /home/$(whoami)/.config/Kvantum/kvantum.kvconfig
	sed -i 's/Mojave-light/Mojave-dark/g' /home/$(whoami)/.gtkrc-2.0
else
	lookandfeeltool --apply com.github.vinceliuice.McMojave-light
	sed -i 's/Mojave-dark/Mojave-light/g' /home/$(whoami)/.config/gtk-3.0/settings.ini
	sed -i 's/McMojave/McMojave-light/g' /home/$(whoami)/.config/Kvantum/kvantum.kvconfig
	sed -i 's/Mojave-dark/Mojave-light/g' /home/$(whoami)/.gtkrc-2.0
fi
