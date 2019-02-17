import os
import shutil
import time
img_list = [r'C:\Users\Nefedov Alex\Desktop\CSapp\app\static\{}.jpg'.format(str(i)) for i in range(1, 9)]
p = r'C:\Users\Nefedov Alex\Desktop\CSapp\app\static\plot.jpg'
i=0

current_dir = os.path.dirname(os.path.abspath(__file__))

img_path = os.path.join(current_dir, 'static')
img_list = [os.path.join(img_path, '%s.jpg' % inx) for inx in range(1, 9)]

p = os.path.join(current_dir, 'static', 'plot.jpg')

while True:
    # if os.path.exists(p):
    #     os.remove(p)
    shutil.copy(img_list[i], p)
    time.sleep(1)
    i+=1
    if i > len(img_list)-1:
        i=0
