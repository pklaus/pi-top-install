# pi-top-install
Do you want to run the standard raspbian jessie on the pi-top?
In this repository you find tips, tricks and scripts to install the necessary capabilities to control
the pi-top hardware using a standard raspbian jessie distribution.

**Install pi-top-hub software**

The pi-top-hub software is required to control the pi-top-hub.

THIS SCRIPT IS EXPERIMENTAL AND NOT FULLY TESTED: USE ONLY AT OUR OWN RISK

**Important, read carefully:** The script uses *sudo apt-get-upgrade* bevore installing the pi-top-hub-software, do not
use *sudo apt-get dist-upgrade* afterwards. Also, make sure that **i2c** and **spi** are enabled in *Raspberry Pi Configuration*.

- Download the repository to your pi-top using the "download zip" button
- Using the file manager, go to your download folder,
 right click on "pi-top-install.zip" and choose "Extract here"
- Open a console window and type the following commands. Answer *Y* several times if asked during the installation, which will take several minutes.

```
  cd Downloads
  cd pi-top-install-master
  chmod +x ./install-pi-top
  ./install-pi-top
```
- Reboot your Raspberry Pi

Now you can check the installation: Shut down the Raspberry Pi. The pi-top hub and the red led on the Raspberry Pi should turn off after a while. **Important:** Install now the battery status display widget to ensure that you do not completely drain the battery.

**Install battery status display widget**

See separate repository https://github.com/rricharz/pi-top-battery-status

You are encouraged to contribute to this repository. See https://guides.github.com/activities/hello-world/
to learn how to create, modify and submit a branch.

The contributions in this repository are distributed in the hope that they will be useful, but WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. The owner of this repository
is not affiliated with pi-top.
