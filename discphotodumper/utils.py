import os

def up_dir(path, times=1):
    for _ in range(times):
        path = os.path.dirname(path)
    return path