import pandas as pd
import networkx as nx
import numpy as np
import matplotlib as plt
from networkx import *
import matplotlib.pyplot as plt
import cv2
import tkinter as tk
from tkinter import BOTH, RIGHT, Y, Entry, Frame, Place, Scrollbar, StringVar, messagebox
import pyttsx3

#Ventana nPrincipal 
Ventana = tk.Tk()
Ventana.title("Busqueda automatizada")
Ventana.geometry('1300x650+30+30')
Ventana.resizable(width=False, height=False)
Ventana.configure(background="dark turquoise")

imagen=tk.PhotoImage(file="al.png")
lbl =tk.Label(Ventana,image=imagen)
lbl.place(x=20,y=20)

origen = StringVar()
origen.set("Origen")
cuadro = tk.Entry(Ventana,textvariable=origen, background="dark turquoise")
cuadro.place(x=1070, y=100, width=200, height=30)

destino = StringVar()
destino.set("Destino")
destino = tk.Entry(Ventana,textvariable=destino, background="dark turquoise")
destino.place(x=1070, y=160, width=200, height=30)


def buscar():
    def agregar_arista(G, u, v, w=1, di=True):
        G.add_edge(u, v, weight=w)

        # Si el grafo no es dirigido
        if not di:
            # Agrego otra arista en sentido contrario
            G.add_edge(v, u, weight=w)


    if __name__ == '__main__':
        # Instantiate the DiGraph
        global G
        G = nx.DiGraph()

        # Add node/edge pairs
        agregar_arista(G, "San lázaro", "Santiago", 7,False)
        agregar_arista(G, "Santa Elena", "Santiago", 4,False)
        agregar_arista(G, "Trinchera", "Santiago", 6,False)
        agregar_arista(G, "Guadalupe", "Santiago", 5,False)
        agregar_arista(G, "San Francisco", "Guadalupe", 2,False)
        agregar_arista(G, "Santa Cruz", "Ceibos", 5,False)
        agregar_arista(G, "Ceibos", "San felipe", 2,False)
        agregar_arista(G, "Ceibos", "Santa bárbara", 3,False)
        agregar_arista(G, "Cepeda", "Miguel H", 1,False)
        agregar_arista(G, "Centro", "Santiago", 2,False)
        agregar_arista(G, "Centro", "Trinchera", 7,False)
        agregar_arista(G, "Centro", "Cepeda", 8,False)
        agregar_arista(G, "Centro", "Santa Cruz", 3,False)
        agregar_arista(G, "Centro", "Guadalupe", 3,False)
        agregar_arista(G, "Centro", "Santa bárbara", 4,False)
        
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        text = "Buscando tu camino, espere un momento por favor"
        engine.say(text)
        engine.runAndWait()

        global djk_path
        djk_path = nx.dijkstra_path(G,origen.get(),destino.get())
        print(djk_path) 



        tem=tk.Label(Ventana,text=f"Pasarás por: {djk_path}", font=("Comic Sans MS",18,"bold"), background="dark turquoise")
        tem.place(x=20, y=570)

        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.say("Pasarás por ")
        engine.say(djk_path)
        engine.runAndWait()

def arbol():
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    text = "Imprimiendo grafo"
    engine.say(text)
    engine.runAndWait()

    ruta1 = G.subgraph(djk_path)
    pos = nx.layout.planar_layout(G)
    nx.draw(ruta1, pos, with_labels=True)
    labels = nx.get_edge_attributes(ruta1, 'weight')
    nx.draw_networkx_edge_labels(ruta1, pos, edge_labels=labels)
    plt.show()


def arbol_entero():
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    text = "Imprimiendo grafo"
    engine.say(text)
    engine.runAndWait()

    nx.draw(G, with_labels=True)
    plt.show()



boton3 = tk.Button(Ventana, text="Buscar",command=buscar, cursor="hand2", bg= "red",width=12, relief="flat",
font=("Comic Sans MS",12,"bold"))
boton3.place(x=1110, y=200)

boton3 = tk.Button(Ventana, text="Grafo ruta",command=arbol, cursor="hand2", bg= "red",width=12, relief="flat",
font=("Comic Sans MS",12,"bold"))
boton3.place(x=1110, y=260)

boton3 = tk.Button(Ventana, text="Grafo Entero",command=arbol_entero, cursor="hand2", bg= "red",width=12, relief="flat",
font=("Comic Sans MS",12,"bold"))
boton3.place(x=1110, y=320)



Ventana.mainloop()