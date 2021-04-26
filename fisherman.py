#! /usr/bin/env python3

from selenium.webdriver import Firefox, FirefoxOptions
from time import sleep
from argparse import ArgumentParser, MetavarTypeHelpFormatter
from requests import get
from re import findall
from form_text import *

module_name = 'FisherMan: Extract information from facebook profiles'
__version__ = '1.0'


class Fisher:
    def __init__(self):
        parser = ArgumentParser(description=f'{module_name} (Version {__version__})',
                                formatter_class=MetavarTypeHelpFormatter)

        parser.add_argument('usr', action='store', metavar='USERS', dest='usr',
                            help='defines one or more users for the search',
                            nargs='+')

        parser.add_argument('--email', action='store', metavar='EMAIL', dest='email',
                            required=False,
                            help='If the profile is blocked, you can define your account, '
                                 'however you have the search user in your friends list.')

        parser.add_argument('--password', action='store', metavar='PASSWORD', dest='pwd',
                            required=False,
                            help='Set the password for your facebook account, '
                                 'this parameter has to be used with --email.')

        parser.add_argument('--browser', '-b', action='store_true', dest='browser',
                            required=False,
                            help='Opens the browser / bot')

        parser.add_argument('--version', action='version',
                            version=f'%(prog)s {__version__}', help='Shows the current version of the program.')

        self.args = parser.parse_args()
        self.site = 'https://facebook.com/'
        self.usrs = self.args.usr
        self.__fake_email__ = 'submarino.sub.aquatico@outlook.com'
        self.__password__ = '0cleptomaniaco0'
        self.data = []

    def update(self):
        try:
            r = get("https://raw.githubusercontent.com/Godofcoffe/Butterfly/main/butterfly.py")

            remote_version = str(findall('__version__ = "(.*)"', r.text)[0])
            local_version = __version__

            if remote_version != local_version:
                print(color_text('yellow', "Update Available!\n" +
                                 f"You are running version {local_version}. Version {remote_version} "
                                 f"is available at https://github.com/Godofcoffe/Butterfly"))
        except Exception as error:
            print(color_text('red', f"A problem occured while checking for an update: {error}"))

    def get_data(self):
        return self.data

    def run(self):
        if self.args.browser:
            options = FirefoxOptions()
            options.add_argument("--headless")
            navegador = Firefox(firefox_options=options)
        else:
            navegador = Firefox()
        navegador.get(self.site)

        email = navegador.find_element_by_name("email")
        pwd = navegador.find_element_by_name("pass")
        ok = navegador.find_element_by_name("login")
        classes = ['ii04i59q', 'a3bd9o3v', 'jq4qci2q', 'oo9gr5id',
                   'dati1w0a', 'tu1s4ah4', 'f7vcsfb0', 'discj3wi']

        print('logging in...')
        email.clear()
        pwd.clear()
        if self.args.email == self.__fake_email__ and self.args.pwd == self.__password__:
            email.send_keys(self.__fake_email__)
            pwd.send_keys(self.__password__)
        else:
            email.send_keys(self.args.email)
            pwd.send_keys(self.args.pwd)
        ok.click()
        sleep(2)
        for usr in self.usrs:
            print(f'Coming in {self.site + usr}')
            navegador.get(f'{self.site + usr}/about')

            sleep(3)
            for c in classes:
                print(f'[ {color_text("blue", "+")} ] collecting data ...')
                try:
                    output = navegador.find_element_by_class_name(c)
                except:
                    print(f'[ {color_text("red", "-")} ] class {c} did not return')
                else:
                    if output:
                        self.data.append(output.text)
                    else:
                        continue
                sleep(1)
