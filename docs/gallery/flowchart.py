# Recreate the flowchart in https://xkcd.com/518/

import SchemDraw
from SchemDraw import flow

d = SchemDraw.Drawing(fontsize=12)
b = d.add(flow.start(2, 1.5), label='START')
d.add(flow.LINE, d='down', l=d.unit/2)
d.add(flow.ARROWHEAD)
d1 = d.add(flow.decision(5, 3.6, responses={'E': 'YES', 'S': 'NO'}), label='DO YOU\nUNDERSTAND\nFLOW CHARTS?')
d.add(flow.LINE, l=d.unit/2)
d.add(flow.ARROWHEAD)
d2 = d.add(flow.decision(5, 3.6, responses={'E': 'YES', 'S': 'NO'}), label='OKAY,\nYOU SEE THE\nLINE LABELED\n"YES"?')
d.add(flow.LINE, l=d.unit/2)
d.add(flow.ARROWHEAD)
d3 = d.add(flow.decision(5, 3.6, responses={'E': 'YES', 'S': 'NO'}), label='BUT YOU\nSEE THE ONES\nLABELED "NO".')

d.add(flow.LINE, xy=d3.E, d='right', l=d.unit/2)
d.add(flow.ARROWHEAD)
d.add(flow.box(2, 1.25), label='WAIT,\nWHAT?', anchor='W')
d.add(flow.LINE, xy=d3.S, d='down', l=d.unit/2)
d.add(flow.ARROWHEAD)
listen = d.add(flow.box(2, 1), label='LISTEN.')
d.add(flow.LINE, xy=listen.E, d='right', l=d.unit/2)
d.add(flow.ARROWHEAD)
hate = d.add(flow.box(2, 1.25), label='I HATE\nYOU.', anchor='W')

d.add(flow.LINE, xy=d1.E, d='right', l=d.unit*3.5)
d.add(flow.ARROWHEAD)
good = d.add(flow.box(2, 1), label='GOOD', anchor='W')
d.add(flow.LINE, xy=d2.E, d='right', l=d.unit*1.5)
d.add(flow.ARROWHEAD)
d4 = d.add(flow.decision(5, 3.6, responses={'E': 'YES', 'S': 'NO'}), label='...AND YOU CAN\nSEE THE ONES\nLABELED "NO"?', anchor='W')

d.add(flow.LINE, xy=d4.E, d='right', tox=good.S)
d.add(flow.LINE, d='up', toy=good.S)
d.add(flow.ARROWHEAD)
d.add(flow.LINE, xy=d4.S, d='down', l=d.unit/2)
d.add(flow.ARROWHEAD)
d5 = d.add(flow.decision(5, 3.6, responses={'E': 'YES', 'S': 'NO'}), label='BUT YOU\nJUST FOLLOWED\nTHEM TWICE!')
d.add(flow.LINE, xy=d5.E, d='right', l=d.unit)
d.add(flow.ARROWHEAD)
question = d.add(flow.box(3.5, 1.75), label="(THAT WASN'T\nA QUESTION.)", anchor='W')
d.add(flow.LINE, xy=d5.S, d='down', l=d.unit/3)
d.add(flow.LINE, d='right', tox=question.S)
d.add(flow.LINE, d='up', toy=question.S)
d.add(flow.ARROWHEAD)

d.add(flow.LINE, d='right', xy=good.E, tox=question.S)
d.add(flow.LINE, d='down', l=d.unit)
d.add(flow.ARROWHEAD)
drink = d.add(flow.box(2, 1.5), label="LET'S GO\nDRINK.")
d.add(flow.LINE, xy=drink.E, d='right', label='6 DRINKS')
d.add(flow.ARROWHEAD)
d.add(flow.box(3.2, 2), label='HEY, I SHOULD\nTRY INSTALLING\nFREEBSD!', anchor='W')
d.add(flow.LINE, xy=question.N, d='up', l=d.unit*.75)
d.add(flow.ARROWHEAD)
screw = d.add(flow.box(2, 1), label='SCREW IT.', anchor='S')
d.add(flow.LINE, xy=screw.N, d='up', toy=drink.S)
d.add(flow.ARROWHEAD)
d.draw()
d.save('flowchart.svg')