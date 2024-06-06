#!/bin/bash

if [[ -f /usr/bin/yum ]]; then
	yum update -y
	yum install -y openssh-server
elif [[ -f /usr/bin/apt ]]; then
	apt update -y
	apt install -y openssh-server
elif [[ -f /usr/bin/zypper ]]; then
	zypper update -y
	zypper install -y openssh-server
fi
