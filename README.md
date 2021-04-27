# FisherMan [![GitHub license](https://img.shields.io/github/license/Godofcoffe/FisherMan)](https://github.com/Godofcoffe/FisherMan/blob/main/LICENSE) ![badge](https://img.shields.io/badge/version-2.0-blue)  ![badge](https://img.shields.io/badge/python-%3E%3D3.8-green)

Search for public profile information on Facebook

## Installation
```
# clone the repo
$ git clone https://github.com/Godofcoffe/FisherMan.git

# change the working directory to FisherMan
$ cd FisherMan

# install the requirements
$ python3 -m pip install -r requirements.txt
```

## Usage
```
$ python3 fisherman.py --help
usage: fisherman.py [-h] [--version] [--email EMAIL] [--password PASSWORD]
                    [--browser] [--use-txt TXT_FILE] [--file-output]
                    [--verbose]
                    USERSNAMES [USERSNAMES ...]

FisherMan: Extract information from facebook profiles (Version 2.0)

positional arguments:
  USERSNAMES            defines one or more users for the search

optional arguments:
  -h, --help            show this help message and exit
  --version             Shows the current version of the program.
  --email EMAIL         If the profile is blocked, you can define your
                        account, however you have the search user in your
                        friends list.
  --password PASSWORD   Set the password for your facebook account, this
                        parameter has to be used with --email.
  --browser, -b         Opens the browser / bot
  --use-txt TXT_FILE    Replaces the USERSNAMES parameter with a user list in
                        a txt
  --file-output, -o     Save the output data to a .txt file
  --verbose, -v, -d, --debug
                        It shows in detail the data search process
```
To search for a user
```
python3 fisherman.py name.surname name2.surname2 name3.surname3
```

the username must be found on the facebook profile link, such as:
```
https://facebook.com/name.profile/
```

It is also possible to load multiple usernames from a .txt file, it can be useful for a kind of brute force:
```
python3 fisherman.py --use-txt filename.txt
```

And with that you can send the output to a txt also using: 
```
python3 fisheman.py --file-output
```

Some profiles are limited to displaying your information for any account, so you can use your account to extract.
Note: this should be used as the last hypothesis and the target profile must be on your friends list:
```
python3 fisherman.py --email youremail@email.com --password yourpass
```

## *This tool only extracts information that is public, not to anything illegal being done that violates German privacy.*
