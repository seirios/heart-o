import wfdb
import numpy as np

conversion_factor = 2000  # units per mV


def load_raw_data(file):
    signal, meta = wfdb.rdsamp(file)
    data = np.array(signal) * conversion_factor
    data = np.int16(data)
    return meta['sig_name'], data


if __name__ == "__main__":
    import sys
    path = sys.argv[1]
    cols, dat = load_raw_data(path + '/' + sys.argv[2])
    np.savetxt(sys.argv[3], dat, delimiter=',', header=','.join(cols), comments='')
