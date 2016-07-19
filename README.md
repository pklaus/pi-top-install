# pi-top-install
Do you want to run the standard raspbian jessie on the pi-top or pi-topCEED?
In this repository you find tips, tricks and scripts to install the necessary capabilities to control
the pi-top hardware using a standard raspbian jessie distribution. Several users have confirmed that the
brightness and shutdown programs also work properly on a pi-topCEED using Raspbian.

**1 - Battery status display widget (released)**

See separate repository https://github.com/rricharz/pi-top-battery-status

This program has been tested on raspbian jessie and should work well with any
distribution. Do not forget to turn **i2c** on in *Menu/Preferences/Raspberry Pi Configuration/Interfaces*.
The program will display the battery status, 
and will shut down the Raspberry Pi if the battery capacity is low and not
charging. But unless you also install 3 (automatic poweroff) it will not be able
to turn off the pi-top hub and the power to the Raspberry Pi. It would therefore
not protect the battery from further depleting.

**2 - program to set the screen brightness (version 1.0, released)**

Usage (new_value is a screen brightness value between 3 and 10):
```
brightness new_value
brightness increase
brightness decrease
```

The keyboard brightness keys will work, if you put the following into the
keyboard section of /home/pi/.config/openbox/lxde-pi-rc.xml:
```
    <keybind key="0xC7">
      <action name="Execute">
        <command>brightness increase</command>
      </action>
    </keybind>
    <keybind key="0xC6">
      <action name="Execute">
        <command>brightness decrease</command>
      </action>
    </keybind>
```

Instead, you can also copy the lxde-pi-rc.xml file found in this repository to /home/pi/.config/openbox


**3 - program and system service to turn the hub-controller off after shutdown (version 1.0, released)**

This program will help to protect your battery by shutting the pi-top-hub-controller
off after a shutdown of the Raspbery Pi

**Installation instructions for 2 and/or 3**

To download this repository, open a terminal and type:
```
cd Downloads
git clone git://github.com/rricharz/pi-top-install
cd pi-top-install
chmod +x install*
```

Make sure that **spi** is turned on in *Menu/Preferences/Raspberry Pi Configuration/Interfaces*.

Make sure that your system is up-to-date:
```
sudo apt-get update
sudo apt-get upgrade
```

If you want to install 3 (automatic poweroff), you also need to make sure that your system
is updated to the newest bootup and shutdown process, called systemd:
```
sudo apt-get dist-upgrade
```

To install 2 (brightness):
```
./install-brightness
```

To install 3 (automatic poweroff)
```
./install-poweroff
```

Your new software will work after the next bootup.

**Instructions to compile the programs**

To compile the  programs (only required if you want to modify the c programs), use
```
make
```
Then use the install scripts again to reinstall the programs

**4 - use the pi-top speaker with Raspbian

With the following instructions you can use omxplayer with Raspbian:

```
cd /boot
sudo nano config.txt
```
Remove the # in front of #hdmi_drive=2

Save and exit the nano editor

Reboot your rpi

Call omxplayer as follow
```
omxplayer -o hdmi filename
```
where filename is the name of he file you want to play

You are encouraged to contribute to this repository. See https://guides.github.com/activities/hello-world/
to learn how to create, modify and submit a branch. Or open an issue in this repository to report problems or suggestions.

The contributions in this repository are distributed in the hope that they will be useful, but WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. The owner of this repository
is not affiliated with pi-top.

For problems and suggestions, please open an issue in this repository.
