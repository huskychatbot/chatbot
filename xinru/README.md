# chatbot
mandarin chatbot
this is where we put out notebooks that summarize each team members's research


Running the train1.py file in the increasing_artificial_data folder

Type in command k when you see the following:

case: None, logdir: cases/None/train1
[0925 17:57:19 @logger.py:94] WRN Log directory cases/None/train1 exists! Please either backup/delete it, or use a new directory.
[0925 17:57:19 @logger.py:96] WRN If you're resuming from a previous run you can choose to keep it.
[0925 17:57:19 @logger.py:97] Select Action: k (keep) / b (backup) / d (delete) / n (new) / q (quit):


And this is the error message I got:

Traceback (most recent call last):

  File "<ipython-input-1-bd2979c5c3de>", line 1, in <module>
    runfile('C:/Users/david/Desktop/Chinese Tutor/deep-voice-conversion-master/train1.py', wdir='C:/Users/david/Desktop/Chinese Tutor/deep-voice-conversion-master')

  File "C:\Users\david\AppData\Local\Programs\Python\Python36\lib\site-packages\spyder_kernels\customize\spydercustomize.py", line 704, in runfile
    execfile(filename, namespace)

  File "C:\Users\david\AppData\Local\Programs\Python\Python36\lib\site-packages\spyder_kernels\customize\spydercustomize.py", line 108, in execfile
    exec(compile(f.read(), filename, 'exec'), namespace)

  File "C:/Users/david/Desktop/Chinese Tutor/deep-voice-conversion-master/train1.py", line 129, in <module>
    train(args, logdir=logdir_train1)

  File "C:/Users/david/Desktop/Chinese Tutor/deep-voice-conversion-master/train1.py", line 111, in train
    launch_train_with_config(train_conf, trainer=trainer)

  File "C:\Users\david\AppData\Local\Programs\Python\Python36\lib\site-packages\tensorpack\train\interface.py", line 88, in launch_train_with_config
    model._build_graph_get_cost, model.get_optimizer)

  File "C:\Users\david\AppData\Local\Programs\Python\Python36\lib\site-packages\tensorpack\utils\argtools.py", line 165, in wrapper
    return func(*args, **kwargs)

  File "C:\Users\david\AppData\Local\Programs\Python\Python36\lib\site-packages\tensorpack\train\tower.py", line 137, in setup_graph
    train_callbacks = self._setup_graph(input, get_cost_fn, get_opt_fn)

  File "C:\Users\david\AppData\Local\Programs\Python\Python36\lib\site-packages\tensorpack\train\trainers.py", line 130, in _setup_graph
    self._make_get_grad_fn(input, get_cost_fn, get_opt_fn), get_opt_fn)

  File "C:\Users\david\AppData\Local\Programs\Python\Python36\lib\site-packages\tensorpack\graph_builder\training.py", line 191, in build
    grads = allreduce_grads(grad_list)

  File "C:\Users\david\AppData\Local\Programs\Python\Python36\lib\site-packages\tensorpack\graph_builder\utils.py", line 94, in allreduce_grads
    from tensorflow.contrib import nccl

ImportError: cannot import name 'nccl'
