import glob
import cv2
files = glob.glob("*")
def aspect(filename):
  im = cv2.imread(filename)
  return float(im.shape[0]) / float(im.shape[1])
aspects = [aspect(f) for f in files]
for f, a in zip(files, aspects):
  if a < 1:
    print(f)
