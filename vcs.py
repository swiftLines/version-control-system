import os
import hashlib
import pickle

def init_vcs():
    os.makedirs('.vcs_storage', exists_ok=True)
    print('VCS initialized.')


def snapshot(directory):
    snapshot_hash = hashlib.sha256()
    snapshot_data = {'files': {}}

    for root, dirs, files in os.walk(directory):
        for file in files:
            if '.vcs_storage' in os.path.join(root, file):
                continue

            file_path = os.path.join(root, file)

            with open(file_path, 'rb') as f:
                content = f.read()
                snapshot_hash.update(content)
                snapshot_data['files'][file_path] = content

    hash_digest = snapshot_hash.hexdigest()
    snapshot_data['file_list'] = list(snapshot_data['files'].keys())

    with open(f'.vcs_storage/{hash_digest}','wb') as f:
        pickle.dump(snapshot_data, f)

    print(f'Snapshot created with hash {hash_digest}')
    