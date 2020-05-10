wetter - weewx extension that sends data to wetter.com
Copyright 2014-2020 Matthew Wall
Distributed under the terms of the GNU Public License (GPLv3)

Installation instructions:

1) download

wget -O weewx-wetter.zip https://github.com/matthewwall/weewx-wetter/archive/master.zip

1) run the installer:

wee_extension -install weewx-wetter.zip

2) modify weewx.conf:

[StdRESTful]
    [[Wetter]]
        username = USERNAME
        password = PASSWORD

3) restart weewx

sudo /etc/init.d/weewx stop
sudo /etc/init.d/weewx start
