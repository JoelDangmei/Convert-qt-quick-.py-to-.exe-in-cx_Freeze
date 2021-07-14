from cx_Freeze import setup, Executable

files = []

target = Executable(
    script="",
    base="Win32GUI",
    icon=""
)

setup(
    name = "",
    version = "1.0",
    description = "",
    author = "",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
)