#!/usr/bin/env python3

import os
#if can read file:
if os.path.isfile('/Users/m_lves/Downloads/toys-datasets/diabetes.data'):
	print('I have a file to process')
	file=open('/Users/m_lves/Downloads/toys-datasets/diabetes.data')
	for line in file.readlines():
        	print(line)
else:
	print('Boo, no file for me.')

