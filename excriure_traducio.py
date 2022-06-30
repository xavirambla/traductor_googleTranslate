#!/usr/bin/python
# -*- coding: UTF-8 -*-
#from input_output import *

import sys
sys.path.insert(0, "../libs")
sys.path.insert(0, "./")
from input_output import *
from translate import Translator

#Rurta absoluta C:\\Users\\Beral Projects\\Desktop\\programas\\

#ruta = "C:\\Users\\Beral Projects\\Desktop\\programas\\traduccio\\"
ruta = "D:/xavi/programas/python/traductor_googleTranslate/"
ruta = "D:\\xavi\\programas\\python\\traductor_googleTranslate\\"

c = Input_output.fileToVariable(ruta+"indexphp - copia.txt")

translator = Translator()
resultado=""
for linea in c.split("\r"):

    linea1 = linea.replace('"','')
    traduccio = translator.translate( linea1, dest = 'fr')
    #print (linea ," : " , traduccio)
    resultado = resultado + linea + ','+'"'+traduccio.text+'"'+"\r"
print (resultado)
    #traduccions = translator.translate(c, dest = 'fr')


#Input_output.addToFile(ruta+'indexphpFr.txt',traduccions.text)

    

    