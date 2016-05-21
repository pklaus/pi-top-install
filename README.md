# pi-top-install
Do you want to run the standard raspbian jessie on the pi-top?
In this repository you find tips, tricks and scripts to install the necessary capabilities to control
the pi-top hardware using a standard raspbian jessie distribution.

**Install battery status display widget (released)**

See separate repository https://github.com/rricharz/pi-top-battery-status

This program has been tested on raspbian jessie and should work well with any distribution. Do not forget to turn **i2c** on in *Raspberry Pi Configuration*. The program also needs i2c-tools installed (install with the command "sudo apt-get install i2c-tools". The program will display the battery status, and will shut down the Raspberry Pi if the battery capacity is low and not charging. But on a standard raspbian system it will not be able to turn off the pi-top hub and the power to the Raspberry Pi. It will therefore not protect the battery from further depleting. The pi-top-hub still needs to be turned off manually with the switch.

You are encouraged to contribute to this repository. See https://guides.github.com/activities/hello-world/
to learn how to create, modify and submit a branch.

The contributions in this repository are distributed in the hope that they will be useful, but WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. The owner of this repository
is not affiliated with pi-top.

For problems and suggestions, please open an issue in this repository.
