import os.path as osp
import numpy as np
from imageio import imread

from dmb.data.datasets.stereo.kitti.base import KittiDatasetBase


class Kitti2012Dataset(KittiDatasetBase):

    def __init__(self, annFile, root, transform=None, toRAM=False):
        super(Kitti2012Dataset, self).__init__(annFile, root, transform, toRAM=toRAM)

    @property
    def name(self):
        return 'KITTI-2012'
