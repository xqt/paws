import os

mylang = 'test'
family = 'wikipedia'


custom_path = os.path.expanduser('~/user-config.py')
if os.path.exists(custom_path):
    with open(custom_path, 'r') as f:
        exec(compile(f.read(), custom_path, 'exec'), globals())

# Clean up temp variables, since pwb issues a warning otherwise
# to help people catch misspelt config
del f
del custom_path

# Things that should be non-easily-overridable
usernames['*']['*'] = os.environ['JPY_USER']