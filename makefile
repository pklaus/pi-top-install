all: brightness poweroff

poweroff: poweroff.c
	gcc -o poweroff poweroff.c -lwiringPi

brightness: brightness.c
	gcc -o brightness brightness.c -lwiringPi
