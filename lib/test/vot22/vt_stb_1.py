import os
import sys
env_path = os.path.join(os.path.dirname(__file__), '../../..')
if env_path not in sys.path:
    sys.path.append(env_path)
from lib.test.vot22.vt_vot22_stb import run_vot_exp
os.environ['CUDA_VISIBLE_DEVICES'] = '0'
run_vot_exp('vtm2', 'v_l_16_384_cornerv3_bs16', vis=False)
