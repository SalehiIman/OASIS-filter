from __future__ import print_function
#%matplotlib 
import pandas as pd
import numpy as np
import os 
import shutil 
import tkinter as tk
from tkinter import filedialog
#_______________________________________________________load .csv file to set the information of current image data set____________________________
win = tk.Tk()
win.withdraw()
win.attributes('-topmost', True)

#ask user to select the location of CSV file containing information of image data set
CsvFile= filedialog.askopenfile(title="select the csv file")
#load csv file 
s=pd.read_csv(CsvFile)
#pd.set_option('display.max_rows', None)

#_______________________________________________________Set the interval for both valence and arousal using a graph showing this two parameter for all images____
"""
Do a mouseclick somewhere, move the mouse to some destination, release
the button.  This class gives click- and release-events and also draws
a line or a box from the click-point to the actual mouseposition
(within the same axes) until the button is released.  Within the
method 'self.ignore()' it is checked whether the button from eventpress
and eventrelease are the same.

"""

from matplotlib.widgets import RectangleSelector
import matplotlib.pyplot as plt
lims={"Valence_cutt_off_lower":0,
      "Valence_cutt_off_upper":0,
      "Arousal_cutt_off_lower":0,
      "Arousal_cutt_off_upper":0
     }
def line_select_callback(eclick, erelease):
    'eclick and erelease are the press and release events'
    x1, y1 = eclick.xdata, eclick.ydata
    x2, y2 = erelease.xdata, erelease.ydata
    lims["Valence_cutt_off_lower"]=x1
    lims["Valence_cutt_off_upper"]=x2
    lims["Arousal_cutt_off_lower"]=y1
    lims["Arousal_cutt_off_upper"]=y2
    
    print("\n                        (%3.2f, %3.2f)     -->       (%3.2f, %3.2f)" % (x1, y1, x2, y2))
    #print("\n Please press Q button to accept the selected area \n otherwise try again to select another interval for valence and arousal")


def toggle_selector(event):
    print(' Key pressed.')
    if event.key in ['Q', 'q'] and toggle_selector.RS.active:
        print('\n      RectangleSelector deactivated.')
        toggle_selector.RS.set_active(False)
        plt.close('all')
    if event.key in ['A', 'a'] and not toggle_selector.RS.active:
        print('\n      RectangleSelector activated.')
        toggle_selector.RS.set_active(True)


fig,current_ax = plt.subplots(figsize=(12, 8))                 # make a new plotting range
txt="\n 1- Set a limit for data to be selected by drawing a box around it;\n to do so, click at the maximum range and and release the mouse where it is supposed to define the minimum value       \n 2- Press Q button to accept the selected area \n otherwise try again to select another interval for valence and arousal"
plt.scatter(s['Valence_mean'], s['Arousal_mean'] ,s=20,facecolors='none', edgecolors='r')
#plt.plot(s['Valence_mean'], s['Arousal_mean'], 'o', markersize=2,face edgecolors='r')
plt.xlabel(r"$Valence$")
plt.ylabel(r"$Arousal$")
plt.xlim(1,7)
plt.ylim(1,7)
#plt.title(r'$title$')
plt.text(1.2, 6.1, txt, style='italic',
        bbox={'facecolor': 'yellow', 'alpha':.2, 'pad': 2})

print("\n      (Minimum Valence,Minimum Arousal)  -->  (Maximum Valence,Maximum Arousal)")

# drawtype is 'box' or 'line' or 'none'
toggle_selector.RS = RectangleSelector(current_ax, line_select_callback,
                                       drawtype='box', useblit=True,
                                       button=[1, 3],  # don't use middle button
                                       minspanx=5, minspany=5,
                                       spancoords='pixels',
                                       interactive=True)
plt.connect('key_press_event', toggle_selector)
#fig.set_size_inches(12, 8, forward=True)
plt.show()

neutral=s[(s['Arousal_mean']<lims["Arousal_cutt_off_upper"])&(s['Arousal_mean']>lims["Arousal_cutt_off_lower"])
          &(s['Valence_mean']<lims["Valence_cutt_off_upper"])&(s['Valence_mean']>lims["Valence_cutt_off_lower"])]
lil=(neutral['Theme'].values)
#len(lil)

#_______________________________________________________ Get the location of image data set and the location for selected images__________________________
root = tk.Tk()
root.withdraw()
root.attributes('-topmost', True)

#filePath = filedialog.askopenfilename()
OASISfolderPath = tk.filedialog.askdirectory(title="select the image data set")


destination = tk.filedialog.askdirectory(title='Where to store final images')
from os import listdir
names=pd.Series(listdir(OASISfolderPath))

for filename in lil:
    # with some images the name added to csv file is different (the difference is about some whitespaces) 
    imageFile = os.path.join(OASISfolderPath, filename+'.jpg')
    if os.path. exists(imageFile):
        shutil.copy(imageFile, destination)
    else:
        ds=(np.where(s['Theme']==filename))
        filename=names[int(ds[0])+1]
        imageFile= os.path.join(OASISfolderPath, filename)  
        shutil.copy(imageFile, destination)
#_______________________________________________________ If we need to rename selected images for using in conditional statement, using final part all selected images from 
#previous stages, would be renamed and coppied to another folder_____________________________ 		
from os.path import isfile
mypathh=filedialog.askdirectory(title='Where to rename images from?')
hh=filedialog.askdirectory(title='Where to save renamed images?')
j=1
for i in listdir(mypathh):
    os.rename((mypathh+r'/'+i),(hh+r'/n%s.jpg')%j)
    j+=1