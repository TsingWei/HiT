import argparse

import os
import sys
prj_path = os.path.join(os.path.dirname(__file__), '..')
if prj_path not in sys.path:
    sys.path.append(prj_path)
import _init_paths

import time
import importlib

import numpy as np
from onnxconverter_common import float16
import onnxruntime
import onnx



def parse_args():
    """
    args for training.
    """
    parser = argparse.ArgumentParser(description='Parse args for training')
    # for train
    parser.add_argument('--script', type=str, default='HiT',
                        help='training script name')
    parser.add_argument('--config', type=str, default='HiT_Base', help='yaml configure file name')
    args = parser.parse_args()

    return args




def evaluate(ort_session, ort_inputs, bs):
    '''Speed Test'''
    T_w = 100
    T_t = 1000
    print("testing speed ...")
    # overall
    for i in range(T_w):
        ort_outs = ort_session.run(None, ort_inputs)
    start = time.time()
    for i in range(T_t):
        ort_outs = ort_session.run(None, ort_inputs)
    end = time.time()
    avg_lat = (end - start) / (T_t * bs)
    print("The average overall latency is %.2f ms" % (avg_lat * 1000))
    print("FPS is %.2f fps" % (1. / avg_lat))



if __name__ == "__main__":
    # Compute the Flops and Params of our STARK-S model
    args = parse_args()
    '''update cfg'''
    '''set some values'''
    bs = 1
    '''get some onnx model'''
    onnx_name = 'checkpoints/train/HiT/HiT_Base/VT_ep1500.onnx'
    onnx_model = onnx.load(onnx_name)
    model_fp16 = float16.convert_float_to_float16(onnx_model)
    onnx.save(model_fp16, "test_net_fp16.onnx")
    ort_session = onnxruntime.InferenceSession("test_net_fp16.onnx",providers=['CUDAExecutionProvider'])
    print(onnxruntime.get_device())
    if args.script == "HiT":
        # get the template and search
        dtype = np.float16
        template = np.random.randn(1, 3, 128, 128).astype(dtype)
        search = np.random.randn(1, 3, 256, 256).astype(dtype)
        ort_inputs = {'search': search,
                      'template': template
                      }
        # evaluate the model properties
        evaluate(ort_session, ort_inputs, bs=bs)
    else:
        raise NotImplementedError
