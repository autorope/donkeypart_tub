import random
import platform
import numpy as np
import pytest
from donkeypart_tub import Tub


def on_pi():
    if 'arm' in platform.machine():
        return True
    return False


@pytest.fixture
def tub_path(tmpdir):
    tub_path = tmpdir.mkdir('tubs').join('tub')
    return str(tub_path)


@pytest.fixture
def tub(tub_path):
    t = create_sample_tub(tub_path, records=10)
    return t


@pytest.fixture
def tubs(tmpdir, tubs=5):
    tubs_dir = tmpdir.mkdir('tubs')
    tub_paths = [ str(tubs_dir.join('tub_{}'.format(i))) for i in range(tubs) ]
    tubs = [ create_sample_tub(tub_path, records=5) for tub_path in tub_paths ]
    return (str(tubs_dir), tub_paths, tubs)


def create_sample_tub(path, records=10):
    inputs=['cam/image_array', 'angle', 'throttle']
    types=['image_array', 'float', 'float']
    t = Tub(path, inputs=inputs, types=types)
    for _ in range(records):
        record = create_sample_record()
        t.put_record(record)
    return t


def create_sample_record():
    img_arr = np.random.randint(0, 255, (120, 160, 3))
    record = {
        'cam/image_array': img_arr,
        'angle': random.uniform(-1, 1),
        'throttle':random.uniform(-1, 1)
    }
    return record


