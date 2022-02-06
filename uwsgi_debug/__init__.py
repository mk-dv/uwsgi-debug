import pydevd_pycharm
pydevd_pycharm.settrace('localhost', port=8001, stdoutToServer=True, stderrToServer=True)