# linktree-bottlepy
bottle template for a linktree

### setup

Before you can use the bottle server make sure you install the dependencies (into a venv named *venv_bottle* ) with `pip` and
copy the template user data file*:
```
python3 -m virtualenv -p python3 venv_bottle
source venv_bottle/bin/activate
pip install -r requirements.txt
cp userdata.py.template userdata.py
```
* some commands can vary on your system (e.g. pip/pip3)

Furthmore you have to add your own profile picture at *static/me.jpg* and add your informations
into the userdata.py file. You can leave the information empty if you do not need them (e.g. if you do not have facebook).

### notes
+ **sname** stands for **shortname** or your **nickname**.
+ the **shebang* for the **gentoken.py** file is python (not python3), this might lead to errors on your systems.


### source

! The template for the linktree website is from this [repository](https://github.com/MichaelBarney/LinkFree/tree/master/Templates/DarkMode) and only slightly modified.
