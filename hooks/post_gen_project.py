import subprocess

subprocess.call(['git', 'init'])
subprocess.call(['poetry', 'install'])
subprocess.call(['poetry', 'run', 'black', '.'])
subprocess.call(['pre-commit', 'install'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])
