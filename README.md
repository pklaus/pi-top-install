# pi-top-install
Do you want to run the standard raspbian jessie on the pi-top?
In this repository you find tips, tricks and scripts to install the necessary capabilities to control
the pi-top hardware using a standard raspbian jessie distribution.

**Install battery status display widget (released)**

See separate repository https://github.com/rricharz/pi-top-battery-status

This program has been tested on raspbian jessie and should work well with any distribution. Do not forget to turn **i2c** on in *Raspberry Pi Configuration*. The program also needs i2c-tools installed (install with the command "sudo apt-get install i2c-tools". The program will display the battery status, and will shut down the Raspberry Pi if the battery capacity is low and not charging. But on a standard raspbian system it will not be able to turn off the pi-top hub and the power to the Raspberry Pi. It will therefore not protect the battery from further depleting. The pi-top-hub still needs to be turned off manually with the switch.

**Install pi-top-hub software (experimental)**

The pi-top-hub software is required to turn the hub off automatically after a shutdown of the Raspberry Pi.

THIS SCRIPT IS EXPERIMENTAL AND NOT FULLY TESTED: USE ONLY AT OUR OWN RISK. UNLESS YOU ARE WILLING TO
EXPERIMENT, YOU MIGHT PREFER TO REMOVE UNWANTED FEATURES FROM PI-TOP-OS (see https://github.com/rricharz/pi-top-just-as-raspbian.git).

IMPORTANT, READ CAREFULLY: Make sure that **i2c** and **spi** are enabled in *Raspberry Pi Configuration*.

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

You are encouraged to contribute to this repository. See https://guides.github.com/activities/hello-world/
to learn how to create, modify and submit a branch.

The contributions in this repository are distributed in the hope that they will be useful, but WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. The owner of this repository
is not affiliated with pi-top.

For problems and suggestions, please open an issue in this repository.
