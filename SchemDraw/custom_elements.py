"""
This file contains custom elements defined by Adriaan Rol and Felix Schmidt
The intention is that these get merged into SchemDraw.elements after cleaning
up so as to merge them into the master of CDelker
"""
import numpy as np
import SchemDraw.elements as e

# TODO: SQUID
# TODO: SQUID with flux bias line
# TODO: SQUID with gate voltage line
# TODO: BIAS_TEE

_gap = [np.nan, np.nan]

# Transmission line
# TODO: it would be nice if it was possible to draw the inner conductor in grey, but I don't see a way to set the edgecolor of paths/poly
_tl_r = .5
tllength = 6
x0 = 0.5+_tl_r
TL = {
    'name': 'TL',
    'paths': [[[0, 0], [x0, 0], _gap, [x0, _tl_r], [tllength-x0-_tl_r, _tl_r], _gap, [x0, -_tl_r], [tllength-x0-_tl_r, -_tl_r], _gap, [tllength-x0-0.25*_tl_r, 0], [tllength-0.5, 0]]],
    'shapes': [
        {'shape': 'arc',
         'center': [x0, 0],
         'theta1': 90,
         'theta2': 270,
         'width': 1.25*_tl_r,
         'height': 2*_tl_r},
        {'shape': 'arc',
         'center': [x0, 0],
         'theta1': -90,
         'theta2': 90,
         'width': 1.25*_tl_r,
         'height': 2*_tl_r},
        {'shape': 'arc',
         'center': [tllength-x0-.5, 0],
         'theta1': -90,
         'theta2': 90,
         'width': 1.25*_tl_r,
         'height': 2*_tl_r}
    ],
    'extend': False
}

# Josephson junction with gate electrode
jjgh = 0.25
jjgc = 0.4
JJG = {
    'name': 'JJG',
    'base': e.JJ,
    'paths': [[[-jjgc, -2*jjgh], [jjgc, -2*jjgh]],
              [[0, -2*jjgh], [0, -4*jjgh]]],
    'lblloc': 'bot',
    'anchors': {'gate': [0, jjgh*-4]}
}

# Low pass filter
LOW_PASS = {
    'name': 'LOW_PASS',
    'base': e.RBOX,
    'paths': [[[0.15, 0.05],
               [0.6, 0.05],
               [0.8, -.15]]]
}

# PI filter
PI_FILTER = {
    'name': 'PI_FILTER',
    'base': e.RBOX,
    'labels': [{'label': '$\pi$', 'pos': [.5, 0]}]
}

# Single port amplifier
AMP = {'name': 'AMP',
       'paths': [[[0, 0],
                  [np.nan, np.nan],
                  [0.7, 0]]],
       'anchors': {'center': [2, 0]},
       'shapes': [{'shape': 'poly', 'xy': np.array([[0.,  0.5],
                                                    [0.7,  0.],
                                                    [0., -0.5]]), 'fill': False}]}


dircoup_w = 2
dircoup_h = .5
h_offset = 0.01

dx = .07
dy = .07

# Directional coupler
DIR_COUP = {
    'name': 'DIR_COUP',
    'paths': [[[0, h_offset], [0, dircoup_h], [dircoup_w, dircoup_h], [dircoup_w, -dircoup_h],
               [0, -dircoup_h], [0, h_offset],  [dircoup_w, h_offset]
               ]],

    'shapes': [{'shape': 'arc',
                'center': [dircoup_w*.9, -dircoup_h],
                'theta1':90, 'theta2':180,
                'width':1, 'height':1,  # 'angle':0,
                },
               {'shape': 'arc',
                'center': [dircoup_w*.1, -dircoup_h],
                'theta1':0, 'theta2':90,
                'width':1, 'height':1,  # 'angle':0,
                },
               {'shape': 'circle',
                'center': [dircoup_w*.333, -dircoup_h],
                'radius':dx,
                'fill': True,
                'fillcolor':'black'
                },
               {'shape': 'circle',
                'center': [dircoup_w*.666, -dircoup_h],
                'radius':dx,
                'fill': True,
                'fillcolor':'black'
                },
               {'shape': 'circle',
                'center': [0, 0],
                'radius':dx,
                'fill': True,
                'fillcolor':'black'
                },
               {'shape': 'circle',
                'center': [dircoup_w, h_offset],
                'radius':dx,
                'fill': True,
                'fillcolor':'black'
                },
               ],
    'anchors': {'port3': [dircoup_w*.333, -dircoup_h], 'port4': [dircoup_w*.666, -dircoup_h]}
}


IQMIXER = {
    'name': 'IQMIXER',
    'base': e.SOURCE,
    'paths': [[[-.35+dx, -.35], [.35+dx, .35],
               [np.nan, np.nan],
               [.35+dx, -.35], [-.35+dx, .35],
               [np.nan, np.nan],
               [0.5, -1], [0.5, -.50],
               [np.nan, np.nan],
               [0.5, .5], [0.5, 1],
               ]]
}

# Isolator
h = .65
ISOLATOR = {
    'name': 'ISOLATOR',
    'base': e.SOURCE,
    'shapes': [{'shape': 'arc', 'center': [.5, 0],
                'width':h, 'height':h, 'theta1':130, 'theta2':320, 'arrow':'ccw'}],  # 'arrow':'cw'}
}

# Circulator
CIRCULATOR = {
    'name': 'CIRCULATOR',
    'base': ISOLATOR,
    'paths': [[[0.5, .5], [0.5, 1],
               ]],
    'anchors': {'port3': [0.5, 1]}
}

# TODO: Circulator 4port
