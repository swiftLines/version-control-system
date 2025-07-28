import os
import hashlib
import pickle

def init_vcs():
    os.makedirs('.vcs_storage', exists_ok=True)
    print('VCS initialized.')


