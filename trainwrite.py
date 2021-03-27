# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 21:26:12 2021

@author: OZLEM
"""
dosya = open('drone_training.txt', 'w')

for i in range(1,1105):
    
    
    satir1 = 'drone_data/drone_images/{}.jpg\n'.format(i)  # yazdirilacak metin
    dosya.write(satir1)  # yazdirma islemi
dosya.close()