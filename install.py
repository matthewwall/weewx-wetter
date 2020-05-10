# installer for wetter.com
# Copyright 2014-2020 Matthew Wall
# Distributed under the terms of the GNU Public License (GPLv3)

from weecfg.extension import ExtensionInstaller

def loader():
    return WetterInstaller()

class WetterInstaller(ExtensionInstaller):
    def __init__(self):
        super(WetterInstaller, self).__init__(
            version="0.6",
            name='wetter',
            description='Upload weather data to wetter.com.',
            author="Matthew Wall",
            author_email="mwall@users.sourceforge.net",
            restful_services='user.wetter.Wetter',
            config={
                'StdRESTful': {
                    'Wetter': {
                        'username': 'INSERT_USERNAME_HERE',
                        'password': 'INSERT_PASSWORD_HERE'}}},
            files=[('bin/user', ['bin/user/wetter.py'])]
            )
