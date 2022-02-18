https://towardsdatascience.com/borderless-tables-detection-with-deep-learning-and-opencv-ebf568580fe2


Steps to install with virtualenvwrapper:

1. Find the location of Python with a specific version:

```
$ which python
/home/USERNAME/.virtualenvs/tf/bin/python
```

The path to Python is a softlink. Use the following command to find where the original file is:


```
$ namei /home/USERNAME/.virtualenvs/tf/bin/python
f: /home/USERNAME/.virtualenvs/tf/bin/python
 d /
 d home
 d USERNAME
 d .virtualenvs
 d tf
 d bin
 l python -> /usr/bin/python3.9
   d /
   d usr
   d bin
   - python3.9

```

Use the path you found `/usr/bin/python3.9` to create a new virtual environment:

```
mkvirtualenv -p /usr/bin/python3.9
```

2. Install required modules

```
pip install tensorflow tf_slim cython
```

3. Clone Tensorflow models

```
git clone https://github.com/tensorflow/models.git
```

4. Install pycocotools

```
sudo apt install python3.9-dev
pip install git+https://github.com/philferriere/cocoapi.git#subdirectory=PythonAPI
```

5. Install CUDA

Follow the tutorial from [here](https://www.tensorflow.org/install/gpu#install_cuda_with_apt).

5. Prepare project dirs

```
cd models/research
cp object_detection/packages/tf2/setup.py .
python setup.py install
python object_detection/builders/model_builder_tf2_test.py
```
