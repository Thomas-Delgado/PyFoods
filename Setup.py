import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "includes": ["tkinter"], "include_files": ['banana.png']}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Refeições",
    version="0.1",
    description="App para digitar seus dados acerca de seus alimentos ingeridos",
    options={"build_exe": build_exe_options},
    executables=[Executable("Refeicoes.py", base=base)]
)

