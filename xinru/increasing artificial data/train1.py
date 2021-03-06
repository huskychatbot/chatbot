# -*- coding: utf-8 -*-
# /usr/bin/python2



# With __future__ module's inclusion, you can use the function in higher
# python version function in older python version.
# you have to use print as a function now, to bring the print function 
# from Python 3 into Python 2.6+.
from __future__ import print_function

# The argparse module makes it easy to write user-friendly command-line interfaces. 
# The program defines what arguments it requires, 
# and argparse will figure out how to parse those out of sys.argv. 
# The argparse module also automatically generates help and usage messages
# and issues errors when users give the program
# invalid arguments.
import argparse

# multiprocessing is a package that supports spawning processes using an API similar to the threading module. 
# The multiprocessing package offers both local and remote concurrency,
# effectively side-stepping the Global Interpreter Lock by using subprocesses instead of threads. 
# Due to this, the multiprocessing module allows the programmer to fully leverage multiple processors on a given machine.
# It runs on both Unix and Windows.
import multiprocessing

# The OS module in Python provides a way of using operating system dependent functionality. 
# The functions that the OS module provides allows you to interface with the 
# underlying operating system that Python is running on – be that Windows, Mac or Linux. 
import os

# Callback is an interface to do everything else besides the training iterations.
from tensorpack.callbacks.saver import ModelSaver

# Restore a tensorflow checkpoint saved by tf.train.Saver or ModelSaver.
from tensorpack.tfutils.sessinit import SaverRestore

# A collection of options to be used for single-cost trainers.
# Note that you do not have to use TrainConfig. You can use the API of Trainer directly, 
# to have more fine-grained control of the training.
from tensorpack.train.interface import TrainConfig

# Train with a TrainConfig and a Trainer, to present the simple and old training interface. 
# It basically does the following 3 things (and you can easily do them by yourself if you need more control):
# Setup the input with automatic prefetching heuristics, from config.data or config.dataflow.
# Call trainer.setup_graph with the input as well as config.model.
# Call trainer.train with rest of the attributes of config.
from tensorpack.train.interface import launch_train_with_config

# Data-parallel training in “replicated” mode, where each GPU contains a 
# replicate of the whole model. 
# It will build one tower on each GPU under its own variable scope. 
# Each gradient update is averaged or summed across or GPUs through NCCL.
from tensorpack.train.trainers import SyncMultiGPUTrainerReplicated

# The logger module itself has the common logging functions of Python’s logging.Logger.
from tensorpack.utils import logger

# Enqueue datapoints from a DataFlow to a TF queue. And the model receives dequeued tensors.
from tensorpack.input_source.input_source import QueueInput

# import files from other written python code
from data_load import Net1DataFlow

# import tensorflow
import params as hp


from models import Net1
import tensorflow as tf

# define the train function with two paramaters (args, logdir)
def train(args, logdir):

    # model
    model = Net1()

    # dataflow
    df = Net1DataFlow(hp.Train1.data_path, hp.Train1.batch_size)

    # set logger for event and model saver
    logger.set_logger_dir(logdir)

    session_conf = tf.ConfigProto(
        gpu_options=tf.GPUOptions(
            allow_growth=True,
        ), allow_soft_placement=True)

    train_conf = TrainConfig(
        model=model,
        data=QueueInput(df(n_prefetch=1000, n_thread=5)),
        callbacks=[
            ModelSaver(checkpoint_dir=logdir),
            # TODO EvalCallback()
        ],
        max_epoch=hp.Train1.num_epochs,
        steps_per_epoch=hp.Train1.steps_per_epoch,
        session_config=session_conf
    )
    ckpt = '{}/{}'.format(logdir,
                          args.ckpt) if args.ckpt else tf.train.latest_checkpoint(logdir)
    if ckpt:
        train_conf.session_init = SaverRestore(ckpt)

    if args.gpu:
        os.environ['CUDA_VISIBLE_DEVICES'] = args.gpu
        train_conf.nr_tower = len(args.gpu.split(','))

    trainer = SyncMultiGPUTrainerReplicated(hp.Train1.num_gpu)

    launch_train_with_config(train_conf, trainer=trainer)


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-case', type=str, help='experiment case name')
    parser.add_argument('-ckpt', help='checkpoint to load model.')
    parser.add_argument('-gpu', help='comma separated list of GPU(s) to use.')
    arguments = parser.parse_args()
    return arguments


if __name__ == '__main__':
    args = get_arguments()
    logdir_train1 = '{}/{}/train1'.format(hp.logdir_path, args.case)

    print('case: {}, logdir: {}'.format(args.case, logdir_train1))

    train(args, logdir=logdir_train1)

    print("Done")
