# Built With

The following software tools are used to edit FISSURE.

## Git

To add a new git submodule for repositories like GNU Radio out-of-tree modules:
```
git submodule add -b maint-3.8 https://github.com/someone/gr-something.git ./Custom_Blocks/maint-3.8/gr-something
```

To submit changes for FISSURE, clone the git repository with the SSH address to avoid errors when doing a push later on. Generate an SSH key and add it to your GitHub access settings.

## Qt Designer

Python2 branch:
```
sudo apt-get install python-qt4 qt4-designer
```

Python3 branches:
```
sudo apt-get install -y build-essential qtcreator qt5-default
```
To launch: `designer`

## Grip

Python2 branch:
```
sudo python2 -m pip install grip
```

Python3 branches:
```
sudo python3 -m pip install grip
```

To convert markdown to html (requires Internet connection): `grip README.md --export README.html`
