# google-autocomplete
Script to get Google's search autocomplete data


## Installation

1. __Clone the repo and change-directory to it__
```console
$ git clone https://github.com/SkullTech/google-autocomplete.git
Cloning into 'google-autocomplete'...
remote: Counting objects: 25, done.
remote: Compressing objects: 100% (17/17), done.
remote: Total 25 (delta 9), reused 22 (delta 7), pack-reused 0
Unpacking objects: 100% (25/25), done.

$ cd google-autocomplete
```

2. __Install requirements__
```console
$ pip3 install -r requirements.txt
```

## Usage

```console
$ python3 autocomplete.py -h 
usage: autocomplete.py [-h] [-i INP] [-o OUT] [-c]

optional arguments:
  -h, --help         show this help message and exit
  -i INP, --inp INP  Input file containing search terms
  -o OUT, --out OUT  Output CSV file
  -c, --cli          If the program is to be run in interactive CLI mode
```
