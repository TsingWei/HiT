from lib.test.evaluation.environment import EnvSettings

def local_env_settings():
    settings = EnvSettings()

    # Set your local paths here.

    settings.davis_dir = ''
    settings.got10k_lmdb_path = '/home/esac/proj/HiT/data/got10k_lmdb'
    settings.got10k_path = '/home/esac/proj/HiT/data/got10k'
    settings.got_packed_results_path = ''
    settings.got_reports_path = ''
    settings.lasot_extension_subset_path = '/home/esac/proj/HiT/data/lasot_extension_subset'
    settings.lasot_lmdb_path = '/home/esac/proj/HiT/data/lasot_lmdb'
    settings.lasot_path = '/home/esac/proj/HiT/data/lasot'
    settings.network_path = '/home/esac/proj/HiT/test/networks'    # Where tracking networks are stored.
    settings.nfs_path = '/home/esac/proj/HiT/data/nfs'
    settings.otb_path = '/home/esac/proj/HiT/data/OTB2015'
    settings.prj_dir = '/home/esac/proj/HiT'
    settings.result_plot_path = '/home/esac/proj/HiT/test/result_plots'
    settings.results_path = '/home/esac/proj/HiT/test/tracking_results'    # Where to store tracking results
    settings.save_dir = '/home/esac/proj/HiT'
    settings.segmentation_path = '/home/esac/proj/HiT/test/segmentation_results'
    settings.tc128_path = '/home/esac/proj/HiT/data/TC128'
    settings.tn_packed_results_path = ''
    settings.tnl2k_path = '/home/esac/proj/HiT/data/tnl2k'
    settings.tpl_path = ''
    settings.trackingnet_path = '/home/esac/proj/HiT/data/trackingnet'
    settings.uav_path = '/home/esac/proj/HiT/data/UAV123'
    settings.vot_path = '/home/esac/proj/HiT/data/VOT2019'
    settings.youtubevos_dir = ''

    return settings

