from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
includefiles = ['README.md', 'LICENSE', 'bin/primitive_darwin_amd64', 'bin/primitive_linux_amd64',
                'bin/primitive_linux_arm', 'bin/primitive_linux_arm64', 'bin/primitive_windows_amd64.exe']
buildOptions = dict(packages=[], excludes=[])

import sys

base = 'Win32GUI' if sys.platform == 'win32' else None

executables = [
    Executable('v3000.py', base=base)
]

setup(name='v3000',
      version='1.1',
      description='Oflline version of vectorizer',
      options=dict(build_exe=buildOptions),
      executables=executables)
