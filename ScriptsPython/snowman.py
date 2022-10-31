import maya.cmds as cmds

bodyOne = cmds.polySphere()
cmds.rename("body1")
cmds.scale(5, 5, 5, 'body1')

bodyTwo = cmds.duplicate('body1')
cmds.rename("body2")
cmds.scale(7, 7, 7, 'body2')

bodyThree = cmds.duplicate('body1')
cmds.rename("body3")
cmds.scale(9, 9, 9, 'body3')

cmds.move(0, 13.3, 0, 'body4')
cmds.move(0, 24, 0, 'body1')



