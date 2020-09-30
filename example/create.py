import h5py
import numpy as np

x = np.random.random([5,5,3])
with h5py.File('data.h5', 'w') as f:
    f['x'] = x
    f.attrs.create('name', 'Sam')
    f.attrs.create('value', '105')
    f['group_1/x'] = np.sum(x, axis=0)
    f['group_1/y'] = np.sum(x**2, axis=0)
    f['group_2/x'] = np.sum(x, axis=0)
    f['group_2/y'] = np.sum(x**2, axis=0)

    f['group_1/group_1_sub/x'] = np.sum(x, axis=0)
    f['group_1/group_1_sub'].attrs.create('name', 'Dan')

