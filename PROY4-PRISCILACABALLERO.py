
from tkinter import *
from tkinter import messagebox

def crearBoton(valor,i):
    return Button(tablero,text=valor,width=5,height=1,font=("Helvetica",15),command=lambda:botonClick(i))

#FUNCION PARA FINALIZAR EL PROGRAMA 
def seguir_o_finalizar():
    global g
    resp= messagebox.askyesno("FINALIZAR", "Quieres continuar?")
    if resp:
        if g:
            inicio()
    else:
        tablero.destroy()
    
    return resp

#FUNCION PARA LIMPIAR LA PANTALLA DE LA PARTIDA EN CURSO
def limpiar_pantalla():
    global g
    resp= messagebox.askyesno("LIMPIAR PANTALLA", "Quieres realizar esta accion?")
    if resp:
        inicio()
    else:
        messagebox._show("OPERACION CANCELADA", "No se realizó ninguna acción.")
    
    return resp

#FUNCION PARA PRESIONAR BOTONES DEL JUEGO
def botonClick(i):
    global jugador, jugadas, X,Y,Z,g
    Z=int(i/16)
    y=i%16
    Y=int(y/4)
    X=y%4
    print('Z='+str(3-Z)+' Y='+str(Y)+ ' X='+str(X))
    textoz=Label(tablero, text='Z='+str(3-Z), font='arial, 40',fg='purple',bg='pink')
    textoz.place(x=0, y=160)
    textox=Label(tablero, text='X='+str(X), font='arial, 40',fg='purple',bg='pink')
    textox.place(x=0, y=0)
    textoy=Label(tablero, text='Y='+str(Y), font='arial, 40',fg='purple',bg='pink')
    textoy.place(x=0, y=80)
    if g:
        seguir_o_finalizar()
        return
    if not jugadas[Z][Y][X]:
        texto=Label(tablero, text='                           ', font='arial, 40',fg='white',bg='pink')
        texto.place(x=200, y=5)
        if jugador==0:
            texto='X'
            jugadas[Z][Y][X]=-1
            botones[i].config(text=texto, font='arial 15',fg='blue')
        else:
            texto='O'
            jugadas[Z][Y][X]=1
            botones[i].config(text=texto, font= 'arial 15',fg='red')
        
        #SI GANO CON JUGADA HORIZONTAL
        if horizontal():
            ganador()
            text=Label(tablero, text='Gano con: jugada frontal horizontal', font='arial, 30',fg='green',bg='pink')
            text.place(x=300, y=500)
            for x in range(4):
                botones[Z*16+Y*4+x].config(text=texto, font='arial 15',fg='purple',bg='cyan')
            return
        
        #SI GANO CON JUGADA VERTICAL
        if vertical():
            ganador()
            text=Label(tablero, text='Gano con: jugada frontal vertical', font='arial, 30',fg='green',bg='pink')
            text.place(x=300, y=500)
            for y in range(4):
                botones[Z*16+y*4+X].config(text=texto, font='arial 15',fg='purple',bg='cyan')
            return
        
        #SI GANO CON JUGADA PROFUNDIDAD
        if profundidad():
            ganador()
            text=Label(tablero, text='Gano con: jugada frontal profundidad', font='arial, 30',fg='green',bg='pink')
            text.place(x=300, y=500)    
            for z in range(4):
                botones[z*16+Y*4+X].config(text=texto, font='arial 15',fg='purple',bg='cyan')
            return
        
        #SI GANO CON JUGADA DIAGONAL FRONTAL CASO 1
        if X==Y and diagonalfrontal1():
            ganador()
            text=Label(tablero, text='Gano con: jugada diagonal frontal', font='arial, 30',fg='green',bg='pink')
            text.place(x=300, y=500)
            
            for x in range(4):
                y=x
                botones[Z*16+y*4+x].config(text=texto, font='arial 15',fg='yellow',bg='green')
            return
        
        #SI GANO CON JUGADA DIAGONAL FRONTAL CASO 2
        if X+Y==3 and diagonalfrontal2():
            ganador()
            text=Label(tablero, text='Gano con: jugada diagonal frontal', font='arial, 30',fg='green',bg='pink')
            text.place(x=300, y=500)
            for x in range(4):
                y=3-x
                botones[Z*16+y*4+x].config(text=texto, font='arial 15',fg='yellow',bg='green')
            return
        
        #SI GANO CON JUGADA DIAGONAL VERTICAL CASO 1
        if Y==Z and diagonalvertical1():
            ganador()
            text=Label(tablero, text='Gano con: jugada diagonal vertical', font='arial, 30',fg='green',bg='pink')
            text.place(x=300, y=500)
            for z in range(4):
                y=z
                botones[z*16+y*4+X].config(text=texto, font='arial 15',fg='cyan',bg='purple')
            return
        
        #SI GANO CON JUGADA DIAGONAL VERTICAL CASO 2
        if Y+Z==3 and diagonalvertical2():
            ganador()
            text=Label(tablero, text='Gano con: jugada diagonal vertical', font='arial, 30',fg='green',bg='pink')
            text.place(x=300, y=500)
            for z in range(4):
                y=3-z
                botones[z*16+y*4+X].config(text=texto, font='arial 15',fg='cyan',bg='purple')
            return       
        
        #SI GANO CON JUGADA DIAGONAL HORIZONTAL CASO 1
        if X==Z and diagonalhorizontal1():
            ganador()
            text=Label(tablero, text='Gano con: jugada diagonal horizontal', font='arial, 30',fg='green',bg='pink')
            text.place(x=300, y=500)
            for x in range(4):
                z=x
                botones[z*16+Y*4+x].config(text=texto, font='arial 15',fg='green',bg='orange')
            return
        
        # SI GANO CON JUGADA HORIZONTAL CASO 2
        if Z+X==3 and diagonalhorizontal2():
            ganador()
            text=Label(tablero, text='Gano con: jugada diagonal horizontal', font='arial, 30',fg='green',bg='pink')
            text.place(x=300, y=500)
            for x in range(4):
                z=3-x
                botones[z*16+Y*4+x].config(text=texto, font='arial 15',fg='green',bg='orange')
            return
        
        #SI GANO CON JUGADA DIAGONAL CRUZADA CASO 1
        if X==Y and diagonalcruzada1():
            ganador()
            text=Label(tablero, text='Gano con: jugada diagonal cruzada', font='arial, 30',fg='green',bg='pink')
            text.place(x=300, y=500)
            for z in range(4):
                x=3-z
                y=3-z
                botones[z*16+y*4+x].config(text=texto, font='arial 15',fg='yellow',bg='black')
            return
        
        #SI GANO CON JUGADA DIAGONAL CRUZADA CASO 2
        if X==Z and diagonalcruzada2():
            ganador()
            text=Label(tablero, text='Gano con: jugada diagonal cruzada', font='arial, 30',fg='green',bg='pink')
            text.place(x=300, y=500)
            for x in range(4):
                z=x
                y=3-x
                botones[z*16+y*4+x].config(text=texto, font='arial 15',fg='yellow',bg='black')
            return
        
        #SI GANO CON JUGADA DIAGONAL CRUZADA CASO 3
        if Y==Z and diagonalcruzada3():
            ganador()
            text=Label(tablero, text='Gano con: jugada diagonal cruzada', font='arial, 30',fg='green',bg='pink')
            text.place(x=300, y=500)
            for y in range(4):
                z=y
                x=3-y
                botones[z*16+y*4+x].config(text=texto, font='arial 15',fg='yellow',bg='black')
            return       

        #SI GANO CON JUGADA DIAGONAL CRUZADA 4
        if Y==Z==X and diagonalcruzada4():
            ganador()
            text=Label(tablero, text='Gano con: jugada diagonal cruzada', font='arial, 30',fg='green',bg='pink')
            text.place(x=300, y=500)
            for y in range(4):
                z=y
                x=y
                botones[z*16+y*4+x].config(text=texto, font='arial 15',fg='yellow',bg='black')
            return
        
        if not g:
            jugador= not jugador
            texto=Label(tablero, text='Jugador '+str(jugador+1), font='arial, 40',fg='purple',bg='pink')
            texto.place(x=500,y=620)
    
    #SI HAY UNA JUGADA INVALIDA
    else:
        texto=Label(tablero, text='Jugada Invalida ',font='arial, 40', fg='purple',bg='pink')
        texto.place(x=200,y=5)
    print(jugadas)


#IMPRIMIR EL JUGADOR QUE GANO LA PARTIDA
def ganador():
    global jugar,g
    texto=Label(tablero,text='Jugador '+str(jugador+1)+' GANO', font='arial, 40',fg='blue',bg='pink')
    texto.place(x=200,y=5)
    g=1



#JUGADAS

#JUGADAS FRONTALES
#CASO FRONTAL HORIZONTAL
def horizontal():
    global Y,Z
    s=0
    for x in range(4):
        s+=jugadas[Z][Y][x]
    print(str(s)+'h')
    if s<4 and s>-4:
        return False
    return True

#CASO FRONTAL VERTICAL
def vertical():
    global X,Z
    s=0
    for y in range(4):
        s+=jugadas[Z][y][X]
    print(str(s)+'v')
    if s<4 and s>-4:
        return False
    return True

#CASO FRONTAL PROFUNDIDAD
def profundidad():
    global X,Y
    s=0
    for z in range(4):
        s+=jugadas[z][Y][X]
    print(str(s)+'p')
    if s<4 and s>-4:
        return False
    return True


#JUGADAS DIAGONALES
#CASOS DE DIAGONALES FRONTALES
def diagonalfrontal1():
    global Z
    s=0
    for x in range(4):
        y=x
        s+=jugadas[Z][y][x]
    print(str(s)+'df1')
    if s<4 and s>-4:
        return False
    return True

def diagonalfrontal2():
    global Z
    s=0
    for x in range(4):
        y=3-x
        s+=jugadas[Z][y][x]
    print(str(s)+'df2')
    if s<4 and s>-4:
        return False
    return True

#CASOS DE DIAGONALES VERTICALES
def diagonalvertical1():
    global X
    s=0
    for y in range(4):
        z=y
        s+=jugadas[z][y][X]
    print(str(s)+'dv1')
    if s<4 and s>-4:
        return False
    return True

def diagonalvertical2():
    global X
    s=0
    for z in range(4):
        y=3-z
        s+=jugadas[z][y][X]
    print(str(s)+'dv2')
    if s<4 and s>-4:
        return False
    return True

#CASOS DE DIAGONALES HORIZONTALES
def diagonalhorizontal1():
    global Y
    s=0
    for x in range(4):
        z=x
        s+=jugadas[z][Y][x]
    print(str(s)+'dh1')
    if s<4 and s>-4:
        return False
    return True

def diagonalhorizontal2():
    global Y
    s=0
    for x in range(4):
        z=3-x
        s+=jugadas[z][Y][x]
    print(str(s)+'dh2')
    if s<4 and s>-4:
        return False
    return True


#JUGADAS DE DIAGONALES CRUZADAS
#CASO 1
def diagonalcruzada1():
    s=0
    for z in range(4):
        x=3-z
        y=3-z
        s+=jugadas[z][y][x]
    print(str(s)+'dc1')
    if s<4 and s>-4:
        return False
    return True

#CASO 2
def diagonalcruzada2():
    s=0
    for x in range(4):
        z=x
        y=3-x
        s+=jugadas[z][y][x]
    print(str(s)+'dc2')
    if s<4 and s>-4:
        return False
    return True

#CASO 3
def diagonalcruzada3():
    s=0
    for y in range(4):
        z=y
        x=3-y
        s+=jugadas[z][y][x]
    print(str(s)+'dc3')
    if s<4 and s>-4:
        return False
    return True

#CASO 4
def diagonalcruzada4():
    s=0
    for y in range(4):
        z=y
        x=y
        s+=jugadas[z][y][x]
    print(str(s)+'dc4')
    if s<4 and s>-4:
        return False
    return True


#INICIO DEL TABLERO DE JUEGO
def inicio():
    global jugadas,X,Y,Z,jugador,g
    for z in range(4):
        for y in range(4):
            for x in range(4):
                jugadas[z][y][x]=0
                botones[z*16+y*4+x].config(text='',font='arial 15',fg='blue',bg='white')
    X=Y=Z=0
    g=jugador=0
    texto=Label(tablero, text='Jugador '+str(jugador+1),font='arial, 40',fg='purple',bg='pink')
    texto.place(x=500,y=620)
    texto=Label(tablero, text='                           ', font='arial, 40',fg='white',bg='pink')
    texto.place(x=200, y=5)
    textoz=Label(tablero, text='Z='+str(Z), font='arial, 40',fg='purple',bg='pink')
    textoz.place(x=0, y=160)
    textox=Label(tablero, text='X='+str(X), font='arial, 40',fg='purple',bg='pink')
    textox.place(x=0, y=0)
    textoy=Label(tablero, text='Y='+str(Y), font='arial, 40',fg='purple',bg='pink')
    textoy.place(x=0, y=80)
    text=Label(tablero, text='                                                                        ', font='arial, 30',fg='green',bg='pink')
    text.place(x=300, y=500)
    
    
#MATRIZ DE JUGADAS DE LA PARTIDA EN CURSO    
jugadas= [ [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
           [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
           [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
           [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]]

#INICIALIZACION DE LA INTERFAZ GRAFICA
botones=[]
g=0
tablero=Tk()
tablero.title('Tic Tac Toe 3D')
tablero.geometry("1040x720+100+5")
tablero.resizable(0,0)
tablero.configure(bg="pink")

    
for b in range(64):
    botones.append(crearBoton(' ',b))
        
contador=0
for z in range(4):
    for y in range(4):
        for x in range(4):
            botones[contador].grid(row=y+z*4,column=x+(3-z)*4)
            contador+=1

#LLAMADA A LA INCIALIZACION DE LA PARTIDA
inicio()
botonsalir= Button(tablero, text='Salir',width=5,height=1,font=("Helvetica",15),command=seguir_o_finalizar,bg='red')
botonsalir.grid(row=0,column=10)
botonlimpia= Button(tablero, text='Limpiar',width=5,height=1,font=("Helvetica",15),command=limpiar_pantalla,bg='cyan')
botonlimpia.grid(row=2,column=10)
tablero.mainloop()