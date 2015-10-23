# !/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on Oct 18, 2015
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
    # show below is not attached as well. (I cost almost 24 hours to  find it out..)
    sys.path.append("/home/bo/.local/lib/python2.7/site-packages")

from insurance import *
from wbcrawler.parser import parse_keyword
from wbcrawler.weibo import sina_login
from wbcrawler.database import register, unregister, create_database
from wbcrawler.log import *

# First Round: 129 minutes

start = datetime.datetime.now()
account = register('local', address, port)
browser = sina_login(account)
try:
    db = create_database(project, address, port)
    for keyword in KEYWORDS:
        round_start = datetime.datetime.now()
        parse_keyword(db, keyword, browser)
        log(NOTICE, 'The completion of processing the keyword "%s". Time: %d sec(s)' % (keyword.decode('utf-8'), int((datetime.datetime.now() - round_start).seconds)))
        # except KeyboardInterrupt, e:
except:
    browser.close()
    log(ERROR, 'An error occurs.', 'Crawler.py')
finally:
    unregister('local', address, port, account)
    log(NOTICE, 'The completion of processing all keywords. Time: %d min(s)' % int((datetime.datetime.now() - start).seconds / 60))

if __name__ == '__main__':
    pass
