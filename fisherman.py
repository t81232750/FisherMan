#! /usr/bin/env python3

from selenium.webdriver import Firefox, FirefoxOptions
from time import sleep
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from requests import get
from re import findall
from form_text import *
from logo import *

module_name = 'FisherMan: Extract information from facebook profiles'
__version__ = "1.3"


class Fisher:
    def __init__(self):
        parser = ArgumentParser(description=f'{module_name} (Version {__version__})',
                                formatter_class=RawDescriptionHelpFormatter)

        parser.add_argument('USERSNAMES', action='store', nargs='+',
                            help='defines one or more users for the search')

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
        self.__fake_email__ = 'submarino.sub.aquatico@outlook.com'
        self.__password__ = '0cleptomaniaco0'
        self.data = []
        print(color_text('white', name))

    @staticmethod
    def update():
        try:
            r = get("https://raw.githubusercontent.com/Godofcoffe/FisherMan/main/fisherman.py")

            remote_version = str(findall('__version__ = "(.*)"', r.text)[0])
            local_version = __version__

            if remote_version != local_version:
                print(color_text('yellow', "Update Available!\n" +
                                 f"You are running version {local_version}. Version {remote_version} "
                                 f"is available at https://github.com/Godofcoffe/FisherMan"))
        except Exception as error:
            print(color_text('red', f"A problem occured while checking for an update: {error}"))

    def get_data(self):
        return self.data

    def run(self):
        if not self.args.browser:
            options = FirefoxOptions()
            options.add_argument("--headless")
            navegador = Firefox(options=options)
        else:
            navegador = Firefox()
        navegador.get(self.site)

        email = navegador.find_element_by_name("email")
        pwd = navegador.find_element_by_name("pass")
        ok = navegador.find_element_by_name("login")
        classes = ['ii04i59q', 'a3bd9o3v', 'jq4qci2q', 'oo9gr5id',
                   'dati1w0a', 'tu1s4ah4', 'f7vcsfb0', 'discj3wi']

        email.clear()
        pwd.clear()
        if self.args.email is None or self.args.pwd is None:
            print(f'logging into the account: {self.__fake_email__}:{self.__password__}')
            email.send_keys(self.__fake_email__)
            pwd.send_keys(self.__password__)
        else:
            print(f'logging into the account: {self.args.email}:{self.args.pwd}')
            email.send_keys(self.args.email)
            pwd.send_keys(self.args.pwd)
        ok.click()
        sleep(1)
        for usr in self.args.USERSNAMES:
            if ' ' in usr:
                usr = str(usr).replace(' ', '.')
            print(f'Coming in {self.site + usr}')
            navegador.get(f'{self.site + usr}/about')

            sleep(3)
            for c in classes:
                try:
                    output = navegador.find_element_by_class_name(c)
                except:
                    print(f'[ {color_text("red", "-")} ] class {c} did not return')
                else:
                    if output:
                        print(f'[ {color_text("blue", "+")} ] collecting data ...')
                        self.data.append(output.text)
                    else:
                        continue
                sleep(1)
        navegador.quit()


fs = Fisher()
fs.update()
fs.run()
stuff = fs.get_data()
print()
print(color_text('green', 'Information found:'))
print('-' * 60)
for st in stuff[6:]:
    print(st)
