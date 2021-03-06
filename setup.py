#!/usr/bin/python
# -*- coding: utf-8 -*-
from distutils.core import setup

setup(name='jolicloud-guestlogin',
      version='0.2-jolicloud0',
      description="A PAM Module for allow guest users to login.",
      long_description="The Module creates a new user and gives it to a guest user.",
      author='Mesutcan Kurt',
      author_email='mesutcank@gmail.com',
      url='http://www.pardus.org.tr',
      license="GPLv2",
      platforms=["Linux"],
      data_files=[('/lib/security', ['guestlogin.py']),
                  ('/etc/security', ['etc/security/guestlogin.conf']),
                  ('/etc/apparmor.d', ['etc/apparmor.d/jolicloud-guest-session']),
                  ('/usr/share/pam-configs', ['pam-configs/guestlogin']),
                  ('/usr/share/jolicloud-guestlogin', ['jolicloud-guestlogin/start-session', 'jolicloud-guestlogin/Xsession']),
                  ('/var/lib/polkit-1/localauthority/90-mandatory.d', ['polkit/org.jolicloud.guestlogin.pkla']),
                  ]
     )



