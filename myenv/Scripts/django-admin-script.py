#!c:\users\ste1546\django\myenv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'django==1.9.3','console_scripts','django-admin'
__requires__ = 'django==1.9.3'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('django==1.9.3', 'console_scripts', 'django-admin')()
    )
