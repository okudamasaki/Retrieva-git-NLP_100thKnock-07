#!/usr/bin/env python
# -*- coding: utf-8 -*-


x = 12
y = u'気温'
z = 22.4

def function(x, y, z):
	return str(x) + u'時の' + str(y) + u'は' + str(z)

print(function(x, y, z))