# # Boulder Opal
from qctrlvisualizer import QCTRL_STYLE_COLORS, plot_controls, get_qctrl_style
from qctrlopencontrols import new_primitive_control
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import jsonpickle
import time
from qctrl import Qctrl

qctrl = Qctrl()
