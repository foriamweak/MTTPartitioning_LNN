# MTTPartitioning_LNN

This is the official repository of source codes, models and dataset for the paper "A Fast Multi-Type Tree Partitioning for Versatile Video Coding with a Lightweight Neural Network," submitted to IEEE Transactions on Multimedia firstly Feb. 23, 2020, and now in press. See the link (https://ieeexplore.ieee.org/document/9277576)

* Executable Files --> "run_windowsEXE" https://github.com/foriamweak/MTTPartitioning_LNN/tree/master/run_windowsEXE
We uploaded executable files with encoding configurations and batch files containing parameters to result in tables of submitted paper. Note that executable files (.exe files) have been compiled using VS 2017 on Windows 10. The base software is VTM 4.0 (official site to download is as follows. https://vcgit.hhi.fraunhofer.de/jvet/VVCSoftware_VTM/-/tags/VTM-4.0)

* Entire Project --> https://github.com/foriamweak/MTTPartitioning_LNN/blob/master/AllProject.7z
This 7-zip file contain the entire project of the proposed method on top of VTM 4.0. When you unzip this file, you additionally need to configure and generate VS2017 solution via CMake.

* Dataset to train --> "dataset"

The dataset has been built during encoding by VTM 4.0. TT_H means the data for horizontal TT split, and TT_V means the data for vertical TT split. This dataset was used to train LNN models defined in the paper.

* LNN model in python --> "model"

Originally, the above dataset has been trained using LNN based on C++, but for those who are not familiar with C++, a python code is shared herein. In this folder, a python code "intraNN_mlp_cpu.py" shows how to build LNN as well as how to prepare the dataset for LNN.

Citation:
S. Park and J. Kang, "Fast Multi-type Tree Partitioning for Versatile Video Coding Using a Lightweight Neural Network," in IEEE Transactions on Multimedia, doi: 10.1109/TMM.2020.3042062.

@ARTICLE{9277576,
  author={S. {Park} and J. {Kang}},
  journal={IEEE Transactions on Multimedia}, 
  title={Fast Multi-type Tree Partitioning for Versatile Video Coding Using a Lightweight Neural Network}, 
  year={2020},
  volume={},
  number={},
  pages={1-1},
  doi={10.1109/TMM.2020.3042062}}
