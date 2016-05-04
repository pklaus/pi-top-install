# pi-top-install
Do you want to run the standard raspbian jessie on the pi-top?
In this repository you find tips, tricks and scripts to install the necessary capabilities to control
the pi-top hardware using a standard raspbian jessie distribution.

You need to have sufficient free space on your sd card. To check, open a terminal window and type

```
df
```

If necessary, you need to expand your file system, using the menu item *Raspberry Pi Configuration*. Also, make sure that
i2c and spi are enabled in *Raspberry Pi Configuration*

**Install pi-top-hub software**

- Download the repository to your pi-top using the "download zip" button
- Using the file manager, go to your download folder,
 right click on "pi-top-install.zip" and choose "Extract here"
- Open a console window and type the following commands

```
  cd Downloads
  cd pi-top-install
  chmod +x ./install-pi-top
  ./install-pi-top
```
- Reboot your Raspberry Pi

**Install battery status display widget**

See separate repository https://github.com/rricharz/pi-top-battery-status

You are encouraged to contribute to this repository. See https://guides.github.com/activities/hello-world/
to learn how to create, modify and submit a branch.

The contributions in this repository are distributed in the hope that they will be useful, but WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. The owner of this repository
is not affiliated with pi-top.
