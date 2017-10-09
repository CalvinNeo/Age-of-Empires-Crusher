#coding: utf8

import shutil
tar = "D:/Games/AOE_UserPatch/Ai/"
shutil.copyfile('Crusher.ai', tar + "Crusher.ai")
shutil.copyfile('Crusher.per', tar + "Crusher.per")
shutil.rmtree(tar + "Crusher")
shutil.copytree('Crusher/', tar + "Crusher")