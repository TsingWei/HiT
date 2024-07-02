class EnvironmentSettings:
    def __init__(self):
        self.workspace_dir = '/home/esac/proj/HiT'    # Base directory for saving network checkpoints.
        self.tensorboard_dir = '/home/esac/proj/HiT/tensorboard'    # Directory for tensorboard files.
        self.pretrained_networks = '/home/esac/proj/HiT/pretrained_networks'
        self.lasot_dir = '/home/esac/proj/HiT/data/lasot'
        self.got10k_dir = '/home/esac/proj/HiT/data/got10k'
        self.lasot_lmdb_dir = '/home/esac/proj/HiT/data/lasot_lmdb'
        self.got10k_lmdb_dir = '/home/esac/proj/HiT/data/got10k_lmdb'
        self.trackingnet_dir = '/home/esac/proj/HiT/data/trackingnet'
        self.trackingnet_lmdb_dir = '/home/esac/proj/HiT/data/trackingnet_lmdb'
        self.coco_dir = '/home/esac/proj/HiT/data/coco'
        self.coco_lmdb_dir = '/home/esac/proj/HiT/data/coco_lmdb'
        self.imagenet1k_dir = '/home/esac/proj/HiT/data/imagenet1k'
        self.lvis_dir = ''
        self.sbd_dir = ''
        self.imagenet_dir = '/home/esac/proj/HiT/data/vid'
        self.imagenet_lmdb_dir = '/home/esac/proj/HiT/data/vid_lmdb'
        self.imagenetdet_dir = ''
        self.ecssd_dir = ''
        self.hkuis_dir = ''
        self.msra10k_dir = ''
        self.davis_dir = ''
        self.youtubevos_dir = ''
