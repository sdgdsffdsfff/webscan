#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Lcy
# @Date:   2015-07-22 10:41:17
# @Last Modified by:   Lcy
# @Last Modified time: 2015-07-22 10:49:44
import sys
from PyQt4 import QtGui
app = QtGui.QApplication(sys.argv)
widget = QtGui.QWidget()
widget.resize(300,300)
widget.setWindowTitle(u"Lcy旁站查询")
widget.show()
sys.exit(app.exec_())