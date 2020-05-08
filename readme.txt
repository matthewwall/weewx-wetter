wetter - weewx extension that sends data to wetter.com
Copyright 2014 Matthew Wall

Installation instructions:

1) run the installer:

wee_extension -install weewx-wetter.tgz

2) modify weewx.conf:

[StdRESTful]
    [[Wetter]]
        username = USERNAME
        password = PASSWORD

3) restart weewx

sudo /etc/init.d/weewx stop
sudo /etc/init.d/weewx start
