# UARTPythonController

Control PC Keyboard via commands from serial communication.

## Installation

First, ensure that you are running python 3.6.x and that you are running on Windows. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install.

```bash
pip install pyHook-1.5.1-cp36-cp36m-win_amd64.whl
pip install -r requirements.txt
```

## Usage

```python
python interface.py
```
The script automatically captures anything sent that ends with the '\n' character and attempts to parse. The types of commands are "press &lt;keycode&gt;" and "release &lt;keycode&gt; ... &lt;keycode&gt;"

Sending a serial command such as "press 32" will have the client hold down the space bar and "release 32 40" would have the client let go of both the space bar and the down arrow key.

## License
[MIT](https://choosealicense.com/licenses/mit/)