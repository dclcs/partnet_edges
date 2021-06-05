def export_ply(out, v):
    with open(out, 'w+') as fout:
        fout.write('ply\n');
        fout.write('format ascii 1.0\n');
        fout.write('element vertex ' + str(v.shape[0]) + '\n');
        fout.write('property float x\n');
        fout.write('property float y\n');
        fout.write('property float z\n');
        fout.write('end_header\n');

        for i in range(v.shape[0]):
            fout.write('%f %f %f\n' % (v[i, 0], v[i, 1], v[i, 2]))



import numpy as np

fn = "sample.npz"

data = np.load(fn)['arr_0']
print(data)

for i in range(data.shape[0]):
  export_ply('ply/{0}.ply'.format(i), data[i])