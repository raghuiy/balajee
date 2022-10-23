import os
#print(type(os.environ.items()))
for k, v in sorted(os.environ.items()):
    print(f'{k}={v}')