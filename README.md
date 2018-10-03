skimage.transform.resize bug

Small project to reproduce a bug in scikit-image

Usage
=====

* Install requirements:
  pip install -r requirements.txt

* Run script on 2 different computers. Tested on two computers running Ubuntu 18.04, one with 4 cores, one with 16 cores.

* Copy results of one computer onto other computer

* Visualize results with python notebook
  jupyter notebook

Results
=======

* Points that are different in both images are showed in Python Notebook with a red cross in plot.
* Mismatching points form lines.
