# Python toolbox

Set of python scripts

### Debian

* Install python 3.6, python3.6 pip, git

#### Add path to python script to ~/.bashrc

Edit your ~/.bashrc with your favourite text editor  
For example to edit your ~/.bashrc with nano run the following command

```
nano ~/.bashrc
```

Then add the following code to your ~/.bashrc and save the file.

```
if [ -d "$HOME/.local/bin" ]; then
   PATH="$HOME/.local/bin:$PATH"
fi
```

Finally source your ~/.bashrc

```
source ~/.bashrc
```

#### Install scripts with pip

Note if you only have python 3.6 install the pip command will be pip and not pip3  
The pip command may also be called pip3.6 on different linux distribution

The quickest way to find to find the name of the pip command on linux is to type pip in the terminal  
and then press the tab key and it will show you a list of the pip commands.

```
pip3 install --user git+https://github.com/NapoleonWils0n/toolbox.git
```

* Upgrade scripts with pip

```
pip3 install --upgrade --user git+https://github.com/NapoleonWils0n/toolbox.git
```



### Freebsd

* Install python 3.6, python3.6 pip, git

```
sudo pkg install python36 py36-pip git
```

You can also use ports to install the required software

#### Add path to python script to ~/.bashrc

Edit your ~/.bashrc with your favourite text editor  
For example to edit your ~/.bashrc with nano run the following command

```
nano ~/.bashrc
```

Then add the following code to your ~/.bashrc and save the file.

```
if [ -d "$HOME/.local/bin" ]; then
   PATH="$HOME/.local/bin:$PATH"
fi
```

Finally source your ~/.bashrc

```
. ~/.bashrc
```

#### Install scripts with pip

```
pip-3.7 install --user git+https://github.com/NapoleonWils0n/toolbox.git
```

* Upgrade scripts with pip

```
pip-3.7 install --upgrade --user git+https://github.com/NapoleonWils0n/toolbox.git
```
