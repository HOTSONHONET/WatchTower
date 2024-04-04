import traceback
import gc

for object in gc.get_objects():
    print(object)