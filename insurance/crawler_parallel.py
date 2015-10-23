# !/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on Oct 16, 2015
@author:       Bo Zhao
@email:        bo_zhao@hks.harvard.edu
@website:      http://yenching.org
@organization: Harvard Kennedy School
'''

import sys
import platform
import os

if "Linux" in platform.platform():
    sys.path.append(os.getcwd())
    # Important: Before deploying the program, compare the deploying version with
    # a normal debugging version, especially checkking which path is not loaded in
    # sys.path. Other than the root of the program, I noticed that another path as
    # show below is not attached as well. (I cost almost 24 hours to find it out..)
    sys.path.append("/home/bo/.local/lib/python2.7/site-packages")

# libraries
from insurance import *
from wbcrawler.parallel import parallel_crawling

repost, path, info = 2, 0, 0

# funcs
try:
    parallel_crawling(4, 0, 0, project, address, port)
except:
    pass

try:
    parallel_crawling(0, 4, 0, project, address, port)
except:
    pass

try:
    parallel_crawling(0, 0, 4, project, address, port)
except:
    pass

if __name__ == '__main__':
    pass
