import openpyxl
from tkinter import *
from tkinter import messagebox


# definimos las funciones del programa

def abrir_topLevel_dias():
    global td
    td = Toplevel()
    td.title("Ingresar Dia")
    td.resizable(False, False)
    td.geometry("300x360")
    td.config(bg="white")

    # cambiamos el icono de la ventana

    td.iconbitmap("C:\\Users\\gerar\\OneDrive\\Documentos\\Programacion\\Proyecto\\img2\\uis2r_qdd_icon.ico")

# fondo

    imagen = PhotoImage(file="img2/fond.png")

    lb_imagen = Label(td, image=imagen)
    lb_imagen.pack()
    lb_imagen.image = imagen

# opciones
    bt_ingresar = Button(td,text="Lunes", command=abrir_topLevel_materia1)
    bt_ingresar.config(bg = "#1e2329",fg="white", font=("Courier", 9, "italic"))
    bt_ingresar.place(x=50, y=20, width=200, height=40)

    bt_ingresar = Button(td,text="Martes", command=abrir_topLevel_materia2)
    bt_ingresar.config(bg = "#1e2329",fg="white", font=("Courier", 9, "italic"))
    bt_ingresar.place(x=50, y=70, width=200, height=40)

    bt_ingresar = Button(td,text="Miercoles", command=abrir_topLevel_materia3)
    bt_ingresar.config(bg = "#1e2329",fg="white", font=("Courier", 9, "italic"))
    bt_ingresar.place(x=50, y=120, width=200, height=40)

    bt_ingresar = Button(td,text="Jueves", command=abrir_topLevel_materia4)
    bt_ingresar.config(bg = "#1e2329",fg="white", font=("Courier", 9, "italic"))
    bt_ingresar.place(x=50, y=170, width=200, height=40)

    bt_ingresar = Button(td,text="Viernes", command=abrir_topLevel_materia5)
    bt_ingresar.config(bg = "#1e2329",fg="white", font=("Courier", 9, "italic"))
    bt_ingresar.place(x=50, y=220, width=200, height=40)

    bt_ingresar = Button(td,text="Sabado", command=abrir_topLevel_materia6)
    bt_ingresar.config(bg = "#1e2329",fg="white", font=("Courier", 9, "italic"))
    bt_ingresar.place(x=50, y=270, width=200, height=40)

    bt_ingresar = Button(td,text="Menu Anterior", command=salir3)
    bt_ingresar.config(bg = "#1e2329",fg="white", font=("Courier", 9, "italic"))
    bt_ingresar.place(x=100, y=320, width=100, height=30)

def abrir_topLevel_dias2():
    global td
    td = Toplevel()
    td.title("Ingresar Dia")
    td.resizable(False, False)
    td.geometry("400x500")
    td.config(bg="white")

    # cambiamos el icono de la ventana

    td.iconbitmap("C:\\Users\\gerar\\OneDrive\\Documentos\\Programacion\\Proyecto\\img2\\uis2r_qdd_icon.ico")

# fondo

    imagen = PhotoImage(file="img2/fond.png")

    lb_imagen = Label(tm, image=imagen)
    lb_imagen.pack()
    lb_imagen.image = imagen

# opciones
    bt_ingresar = Button(td,text="Lunes", command=borrar1)
    bt_ingresar.config(bg = "#1e2329",fg="white", font=("Courier", 9, "italic"))
    bt_ingresar.place(x=100, y=130, width=200, height=40)

    bt_ingresar = Button(td,text="Martes", command=borrar2)
    bt_ingresar.config(bg = "#1e2329",fg="white", font=("Courier", 9, "italic"))
    bt_ingresar.place(x=100, y=180, width=200, height=40)

    bt_ingresar = Button(td,text="Miercoles", command=borrar3)
    bt_ingresar.config(bg = "#1e2329",fg="white", font=("Courier", 9, "italic"))
    bt_ingresar.place(x=100, y=230, width=200, height=40)

    bt_ingresar = Button(td,text="Jueves", command=borrar4)
    bt_ingresar.config(bg = "#1e2329",fg="white", font=("Courier", 9, "italic"))
    bt_ingresar.place(x=100, y=280, width=200, height=40)

    bt_ingresar = Button(td,text="Viernes", command=borrar5)
    bt_ingresar.config(bg = "#1e2329",fg="white", font=("Courier", 9, "italic"))
    bt_ingresar.place(x=100, y=330, width=200, height=40)

    bt_ingresar = Button(td,text="Sabado", command=borrar6)
    bt_ingresar.config(bg = "#1e2329",fg="white", font=("Courier", 9, "italic"))
    bt_ingresar.place(x=100, y=380, width=200, height=40)

    bt_ingresar = Button(td,text="Menu Anterior", command=salir3)
    bt_ingresar.config(bg = "#1e2329",fg="white", font=("Courier", 9, "italic"))
    bt_ingresar.place(x=150, y=460, width=100, height=30)

    lb_m = Label(td, text = "Haz click al boton para borrar la Informacion\n almacenada en ese dia")
    lb_m.config(bg="white", fg="#1e2329", font=("Courier", 10, "italic"))
    lb_m.place(x=12.5, y=20)

def abrir_topLevel_materia1():
    global tm
    tm = Toplevel()
    tm.title("Ingresar Materia")
    tm.resizable(False, False)
    tm.geometry("300x360")
    tm.config(bg="white")

    # cambiamos el icono de la ventana

    tm.iconbitmap("C:\\Users\\gerar\\OneDrive\\Documentos\\Programacion\\Proyecto\\img2\\uis2r_qdd_icon.ico")

    # fondo

    imagen = PhotoImage(file="img2/fondm.png")

    lb_imagen = Label(tm, image=imagen)
    lb_imagen.pack()
    lb_imagen.image = imagen

    # informacion

    lb_m = Label(tm, text = "Ingresar Materia y Hora")
    lb_m.config(bg="#1e2329", fg="white", font=("Courier", 12, "italic"))
    lb_m.place(x=35, y=10)
    
    lb_m = Label(tm, text = "⦿ Calculo  ⦿ Algebra ")
    lb_m.config(bg="white", fg="#1e2329", font=("Courier", 16))
    lb_m.place(x=10, y=50)

    lb_m = Label(tm, text = "⦿ Programación")
    lb_m.config(bg="white", fg="#1e2329", font=("Courier", 16))
    lb_m.place(x=10, y=80)

    lb_m = Label(tm, text = "⦿ Lenguaje ⦿ Deportes")
    lb_m.config(bg="white", fg="#1e2329", font=("Courier", 16))
    lb_m.place(x=10, y=110)

    lb_m = Label(tm, text = "⦿ Química  ⦿ Catedra")
    lb_m.config(bg="white", fg="#1e2329", font=("Courier", 16))
    lb_m.place(x=10, y=140)

    entry_m = Entry(tm, textvariable=l)
    entry_m.config(bg="#1e2329", fg="white", font=("Courier", 16))
    entry_m.config(insertbackground="white",justify="center")
    entry_m.focus_set()
    entry_m.place(x=17,y=190)

    bt_g = Button(tm,text="Guardar", command=guardar)
    bt_g.config(bg = "#1e2329",fg="white", font=("Courier", 9, "italic"))
    bt_g.place(x=80, y=240, width=140,height=50)

    bt_m = Button(tm,text="Menu Anterior", command=salir2)
    bt_m.config(bg = "#1e2329",fg="white", font=("Courier", 9, "italic"))
    bt_m.place(x=100, y=320, width=100,height=30)

def guardar():
    global dato1
    dato1 = l.get()

def abrir_topLevel_materia2():
    global tm
    tm = Toplevel()
    tm.title("Ingresar Materia")
    tm.resizable(False, False)
    tm.geometry("300x360")
    tm.config(bg="white")

    # cambiamos el icono de la ventana

    tm.iconbitmap("C:\\Users\\gerar\\OneDrive\\Documentos\\Programacion\\Proyecto\\img2\\uis2r_qdd_icon.ico")
    
      # fondo

    imagen = PhotoImage(file="img2/fondm.png")

    lb_imagen = Label(tm, image=imagen)
    lb_imagen.pack()
    lb_imagen.image = imagen

    # informacion

    lb_m = Label(tm, text = "Ingresar Materia y Hora")
    lb_m.config(bg="#1e2329", fg="white", font=("Courier", 12, "italic"))
    lb_m.place(x=35, y=10)
    
    lb_m = Label(tm, text = "⦿ Calculo  ⦿ Algebra ")
    lb_m.config(bg="white", fg="#1e2329", font=("Courier", 16))
    lb_m.place(x=10, y=50)

    lb_m = Label(tm, text = "⦿ Programación")
    lb_m.config(bg="white", fg="#1e2329", font=("Courier", 16))
    lb_m.place(x=10, y=80)

    lb_m = Label(tm, text = "⦿ Lenguaje ⦿ Deportes")
    lb_m.config(bg="white", fg="#1e2329", font=("Courier", 16))
    lb_m.place(x=10, y=110)

    lb_m = Label(tm, text = "⦿ Química  ⦿ Catedra")
    lb_m.config(bg="white", fg="#1e2329", font=("Courier", 16))
    lb_m.place(x=10, y=140)

    entry_m = Entry(tm, textvariable=ma)
    entry_m.config(bg="#1e2329", fg="white", font=("Courier", 16))
    entry_m.config(insertbackground="white",justify="center")
    entry_m.focus_set()
    entry_m.place(x=17,y=190)

    bt_g = Button(tm,text="Guardar", command=guardar)
    bt_g.config(bg = "#1e2329",fg="white", font=("Courier", 9, "italic"))
    bt_g.place(x=80, y=240, width=140,height=50)

    bt_m = Button(tm,text="Menu Anterior", command=salir2)
    bt_m.config(bg = "#1e2329",fg="white", font=("Courier", 9, "italic"))
    bt_m.place(x=100, y=320, width=100,height=30)

def guardar():
    global dato2
    dato2 = ma.get()

def abrir_topLevel_materia3():
    global tm
    tm = Toplevel()
    tm.title("Ingresar Materia")
    tm.resizable(False, False)
    tm.geometry("300x360")
    tm.config(bg="white")

    # cambiamos el icono de la ventana

    tm.iconbitmap("C:\\Users\\gerar\\OneDrive\\Documentos\\Programacion\\Proyecto\\img2\\uis2r_qdd_icon.ico")
    
      # fondo

    imagen = PhotoImage(file="img2/fondm.png")

    lb_imagen = Label(tm, image=imagen)
    lb_imagen.pack()
    lb_imagen.image = imagen

    # informacion

    lb_m = Label(tm, text = "Ingresar Materia y Hora")
    lb_m.config(bg="#1e2329", fg="white", font=("Courier", 12, "italic"))
    lb_m.place(x=35, y=10)
    
    lb_m = Label(tm, text = "⦿ Calculo  ⦿ Algebra ")
    lb_m.config(bg="white", fg="#1e2329", font=("Courier", 16))
    lb_m.place(x=10, y=50)

    lb_m = Label(tm, text = "⦿ Programación")
    lb_m.config(bg="white", fg="#1e2329", font=("Courier", 16))
    lb_m.place(x=10, y=80)

    lb_m = Label(tm, text = "⦿ Lenguaje ⦿ Deportes")
    lb_m.config(bg="white", fg="#1e2329", font=("Courier", 16))
    lb_m.place(x=10, y=110)

    lb_m = Label(tm, text = "⦿ Química  ⦿ Catedra")
    lb_m.config(bg="white", fg="#1e2329", font=("Courier", 16))
    lb_m.place(x=10, y=140)

    entry_m = Entry(tm, textvariable=mi)
    entry_m.config(bg="#1e2329", fg="white", font=("Courier", 16))
    entry_m.config(insertbackground="white",justify="center")
    entry_m.focus_set()
    entry_m.place(x=17,y=190)

    bt_g = Button(tm,text="Guardar", command=guardar)
    bt_g.config(bg = "#1e2329",fg="white", font=("Courier", 9, "italic"))
    bt_g.place(x=80, y=240, width=140,height=50)

    bt_m = Button(tm,text="Menu Anterior", command=salir2)
    bt_m.config(bg = "#1e2329",fg="white", font=("Courier", 9, "italic"))
    bt_m.place(x=100, y=320, width=100,height=30)

def guardar():
    global dato3
    dato3 = mi.get()

def abrir_topLevel_materia4():
    global tm
    tm = Toplevel()
    tm.title("Ingresar Materia")
    tm.resizable(False, False)
    tm.geometry("300x360")
    tm.config(bg="white")

    # cambiamos el icono de la ventana

    tm.iconbitmap("C:\\Users\\gerar\\OneDrive\\Documentos\\Programacion\\Proyecto\\img2\\uis2r_qdd_icon.ico")
    
      # fondo

    imagen = PhotoImage(file="img2/fondm.png")

    lb_imagen = Label(tm, image=imagen)
    lb_imagen.pack()
    lb_imagen.image = imagen

    # informacion

    lb_m = Label(tm, text = "Ingresar Materia y Hora")
    lb_m.config(bg="#1e2329", fg="white", font=("Courier", 12, "italic"))
    lb_m.place(x=35, y=10)
    
    lb_m = Label(tm, text = "⦿ Calculo  ⦿ Algebra ")
    lb_m.config(bg="white", fg="#1e2329", font=("Courier", 16))
    lb_m.place(x=10, y=50)

    lb_m = Label(tm, text = "⦿ Programación")
    lb_m.config(bg="white", fg="#1e2329", font=("Courier", 16))
    lb_m.place(x=10, y=80)

    lb_m = Label(tm, text = "⦿ Lenguaje ⦿ Deportes")
    lb_m.config(bg="white", fg="#1e2329", font=("Courier", 16))
    lb_m.place(x=10, y=110)

    lb_m = Label(tm, text = "⦿ Química  ⦿ Catedra")
    lb_m.config(bg="white", fg="#1e2329", font=("Courier", 16))
    lb_m.place(x=10, y=140)

    entry_m = Entry(tm, textvariable=j)
    entry_m.config(bg="#1e2329", fg="white", font=("Courier", 16))
    entry_m.config(insertbackground="white",justify="center")
    entry_m.focus_set()
    entry_m.place(x=17,y=190)

    bt_g = Button(tm,text="Guardar", command=guardar)
    bt_g.config(bg = "#1e2329",fg="white", font=("Courier", 9, "italic"))
    bt_g.place(x=80, y=240, width=140,height=50)

    bt_m = Button(tm,text="Menu Anterior", command=salir2)
    bt_m.config(bg = "#1e2329",fg="white", font=("Courier", 9, "italic"))
    bt_m.place(x=100, y=320, width=100,height=30)

def guardar():
    global dato4
    dato4 = j.get()

def abrir_topLevel_materia5():
    global tm
    tm = Toplevel()
    tm.title("Ingresar Materia")
    tm.resizable(False, False)
    tm.geometry("300x360")
    tm.config(bg="white")

    # cambiamos el icono de la ventana

    tm.iconbitmap("C:\\Users\\gerar\\OneDrive\\Documentos\\Programacion\\Proyecto\\img2\\uis2r_qdd_icon.ico")
    
      # fondo

    imagen = PhotoImage(file="img2/fondm.png")

    lb_imagen = Label(tm, image=imagen)
    lb_imagen.pack()
    lb_imagen.image = imagen

    # informacion

    lb_m = Label(tm, text = "Ingresar Materia y Hora")
    lb_m.config(bg="#1e2329", fg="white", font=("Courier", 12, "italic"))
    lb_m.place(x=35, y=10)
    
    lb_m = Label(tm, text = "⦿ Calculo  ⦿ Algebra ")
    lb_m.config(bg="white", fg="#1e2329", font=("Courier", 16))
    lb_m.place(x=10, y=50)

    lb_m = Label(tm, text = "⦿ Programación")
    lb_m.config(bg="white", fg="#1e2329", font=("Courier", 16))
    lb_m.place(x=10, y=80)

    lb_m = Label(tm, text = "⦿ Lenguaje ⦿ Deportes")
    lb_m.config(bg="white", fg="#1e2329", font=("Courier", 16))
    lb_m.place(x=10, y=110)

    lb_m = Label(tm, text = "⦿ Química  ⦿ Catedra")
    lb_m.config(bg="white", fg="#1e2329", font=("Courier", 16))
    lb_m.place(x=10, y=140)

    entry_m = Entry(tm, textvariable=v)
    entry_m.config(bg="#1e2329", fg="white", font=("Courier", 16))
    entry_m.config(insertbackground="white",justify="center")
    entry_m.focus_set()
    entry_m.place(x=17,y=190)

    bt_g = Button(tm,text="Guardar", command=guardar)
    bt_g.config(bg = "#1e2329",fg="white", font=("Courier", 9, "italic"))
    bt_g.place(x=80, y=240, width=140,height=50)

    bt_m = Button(tm,text="Menu Anterior", command=salir2)
    bt_m.config(bg = "#1e2329",fg="white", font=("Courier", 9, "italic"))
    bt_m.place(x=100, y=320, width=100,height=30)

def guardar():
    global dato5
    dato5 = v.get()

def abrir_topLevel_materia6():
    global tm
    tm = Toplevel()
    tm.title("Ingresar Materia")
    tm.resizable(False, False)
    tm.geometry("300x360")
    tm.config(bg="white")

    # cambiamos el icono de la ventana

    tm.iconbitmap("C:\\Users\\gerar\\OneDrive\\Documentos\\Programacion\\Proyecto\\img2\\uis2r_qdd_icon.ico")
    
    # fondo

    imagen = PhotoImage(file="img2/fondm.png")

    lb_imagen = Label(tm, image=imagen)
    lb_imagen.pack()
    lb_imagen.image = imagen

    # informacion

    lb_m = Label(tm, text = "Ingresar Materia y Hora")
    lb_m.config(bg="#1e2329", fg="white", font=("Courier", 12, "italic"))
    lb_m.place(x=35, y=10)
    
    lb_m = Label(tm, text = "⦿ Calculo  ⦿ Algebra ")
    lb_m.config(bg="white", fg="#1e2329", font=("Courier", 16))
    lb_m.place(x=10, y=50)

    lb_m = Label(tm, text = "⦿ Programación")
    lb_m.config(bg="white", fg="#1e2329", font=("Courier", 16))
    lb_m.place(x=10, y=80)

    lb_m = Label(tm, text = "⦿ Lenguaje ⦿ Deportes")
    lb_m.config(bg="white", fg="#1e2329", font=("Courier", 16))
    lb_m.place(x=10, y=110)

    lb_m = Label(tm, text = "⦿ Química  ⦿ Catedra")
    lb_m.config(bg="white", fg="#1e2329", font=("Courier", 16))
    lb_m.place(x=10, y=140)

    entry_m = Entry(tm, textvariable=s)
    entry_m.config(bg="#1e2329", fg="white", font=("Courier", 16))
    entry_m.config(insertbackground="white",justify="center")
    entry_m.focus_set()
    entry_m.place(x=17,y=190)

    bt_g = Button(tm,text="Guardar", command=guardar)
    bt_g.config(bg = "#1e2329",fg="white", font=("Courier", 9, "italic"))
    bt_g.place(x=80, y=240, width=140,height=50)

    bt_m = Button(tm,text="Menu Anterior", command=salir2)
    bt_m.config(bg = "#1e2329",fg="white", font=("Courier", 9, "italic"))
    bt_m.place(x=100, y=320, width=100,height=30)

def guardar():
    global dato6
    dato6 = s.get()

def salir2():
    tm.destroy()


def salir3():
    td.destroy()

def salir4():
    mh.destroy()


def salir():
    ventana_principal.destroy()

def ver1():
     g = str(l.get())
     if g==1:
        g = g
     m_resultados1.insert(INSERT, f"\n{g}")

     o = str(ma.get())
     if o==1:
        o = o
     m_resultados2.insert(INSERT, f"\n{o}")

     u = str(mi.get())
     if u==1:
        u = u
     m_resultados3.insert(INSERT, f"\n{u}")

     k = str(j.get())
     if k==1:
        k = k
     m_resultados4.insert(INSERT, f"\n{k}")

     b = str(v.get())
     if b==1:
        b = b
     m_resultados5.insert(INSERT, f"\n{b}")

     x = str(s.get())
     if x==1:
        x = x
     m_resultados6.insert(INSERT, f"\n{x}")


# definimos la funcion para ver horarios
def mostrar():
    global mh
    global m_resultados1
    global m_resultados2
    global m_resultados3
    global m_resultados4
    global m_resultados5
    global m_resultados6
    mh = Toplevel()
    mh.title("Ver Horario Actual")
    mh.resizable(False, False)
    mh.geometry("1300x600")
    mh.config(bg="white")

    # cambiamos el icono de la ventana

    mh.iconbitmap("C:\\Users\\gerar\\OneDrive\\Documentos\\Programacion\\Proyecto\\img2\\uis2r_qdd_icon.ico")

    mii_color = '#010202'
    
    imagen = PhotoImage(file="img2/canv.png")

    lb_imagen = Label(mh, image=imagen)
    lb_imagen.pack()
    lb_imagen.image = imagen

    lb_m = Label(mh, text = " ⦿ Lunes        ⦿ Martes       ⦿ Miercoles    ⦿ Jueves       ⦿ Viernes      ⦿ Sabado")
    lb_m.config(bg='#010202',fg="white", font=("Courier", 16))
    lb_m.place(x=50, y=10)

    bt_m = Button(mh,text="Menu Anterior", command=salir4)
    bt_m.config(bg = "#1e2329",fg="white", font=("Courier", 9, "italic"))
    bt_m.place(x=600, y=560, width=100,height=30)

    bt_m = Button(mh,text="Ver", command=ver1)
    bt_m.config(bg = "#1e2329",fg="white", font=("Courier", 9, "italic"))
    bt_m.place(x=880, y=560, width=100,height=30)

    m_resultados1 = Text(mh)
    m_resultados1.config(bg="#1e2329", fg="white", font=("Courier", 18))
    m_resultados1.place(x=70,y=40,width=140,height=500)

    m_resultados2 = Text(mh)
    m_resultados2.config(bg="#1e2329", fg="white", font=("Courier", 18))
    m_resultados2.place(x=270,y=40,width=140,height=500)

    m_resultados3 = Text(mh)
    m_resultados3.config(bg="#1e2329", fg="white", font=("Courier", 18))
    m_resultados3.place(x=475,y=40,width=140,height=500)

    m_resultados4 = Text(mh)
    m_resultados4.config(bg="#1e2329", fg="white", font=("Courier", 18))
    m_resultados4.place(x=680,y=40,width=140,height=500)

    m_resultados5 = Text(mh)
    m_resultados5.config(bg="#1e2329", fg="white", font=("Courier", 18))
    m_resultados5.place(x=880,y=40,width=140,height=500)

    m_resultados6 = Text(mh)
    m_resultados6.config(bg="#1e2329", fg="white", font=("Courier", 18))
    m_resultados6.place(x=1080,y=40,width=140,height=500)


# definimos la funcion de borrar
def borrar1():
    l.set("")
    m_resultados1.delete
def borrar2():
    ma.set("")
    m_resultados2.delete
def borrar3():
    mi.set("")
    m_resultados3.delete
def borrar4():
    j.set("")
    m_resultados4.delete
def borrar5():
    v.set("")
    m_resultados5.delete
def borrar6():
    s.set("")
    m_resultados6.delete

def borrarprueba():
    abrir_topLevel_dias2()


def excel():
 libro = openpyxl.Workbook()

# Obtener la hoja activa del libro
 hoja_activa = libro.active

# Establecer encabezados de columna
 hoja_activa['A1'] = "Lunes"
 hoja_activa['B1'] = "Martes"
 hoja_activa['C1'] = "Miercoles"
 hoja_activa['D1'] = "Jueves"
 hoja_activa['E1'] = "Viernes"
 hoja_activa['F1'] = "Sabado"

# Asignar los valores de las variables a las celdas correspondientes
 hoja_activa['A2'] = str(l.get())
 hoja_activa['B2'] = str(ma.get())
 hoja_activa['C2'] = str(mi.get())
 hoja_activa['D2'] = str(j.get())
 hoja_activa['E2'] = str(v.get())
 hoja_activa['F2'] = str(s.get())

# Guardar el libro de Excel
 libro.save("datos.xlsx")



# creamos la ventana principal

ventana_principal = Tk()
ventana_principal.title("Sistema Horarios")


# tamaño de la ventana
ventana_principal.geometry("1520x855")

# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana
ventana_principal.config(bg="green2")

# cambiamos el icono de la ventana

ventana_principal.iconbitmap("C:\\Users\\gerar\\OneDrive\\Documentos\\Programacion\\Proyecto\\img2\\uis2r_qdd_icon.ico")

# definimos variables globales
l = StringVar()
ma = StringVar()
mi = StringVar()
j = StringVar()
v = StringVar()
s = StringVar()
# frame principal

frame_principal = Frame(ventana_principal)
frame_principal.config(bg="white", width=1580, height=855)
frame_principal.place(x=0, y=0)

# fondo de la app

fondo = PhotoImage(file="img/52686.png")
lb_fondo = Label(frame_principal, image=fondo, bg="white")
lb_fondo.place(x=0,y=0)

# logo uis

fon = PhotoImage(file="img/uis2r.png")
lb_fondo = Label(frame_principal, image=fon)
lb_fondo.place(x=950,y=400)

# definimos colores a usar

mi_color = "#1e2329"
mi_color = "#c8c3bf"
# creamos el titulo

titulo = Label(frame_principal, text="Organizador de Horarios")
titulo.config(bg = "#1e2329",fg="white", font=("Courier", 16, "italic"))
titulo.place(x=40,y=10)

t_info = Label(frame_principal, text="Menu")
t_info.config(bg="#c8c3bf", fg="black", font=("Courier", 24, "italic"))
t_info.place(x=380,y=280,width=300,height=80)

# creamos los botones

bt_ingresar = Button(frame_principal,text="Ingresar Actividad", command=abrir_topLevel_dias)
bt_ingresar.config(bg = "#1e2329",fg="white", font=("Courier", 9, "italic"))
bt_ingresar.place(x=455, y=380, width=150, height=50)

bt_verhorario = Button(frame_principal,text="Ver Horario", command=mostrar)
bt_verhorario.config(bg = "#1e2329",fg="white", font=("Courier", 9, "italic"))
bt_verhorario.place(x=455, y=440, width=150, height=50)

bt_borrar = Button(frame_principal,text="Borrar Actividad", command=borrarprueba)
bt_borrar.config(bg = "#1e2329",fg="white", font=("Courier", 9, "italic"))
bt_borrar.place(x=455, y=500, width=150, height=50)

bt_excel = Button(frame_principal,text="Generar Excel", command=excel)
bt_excel.config(bg = "#1e2329",fg="white", font=("Courier", 9, "italic"))
bt_excel.place(x=455, y=560, width=150, height=50)

bt_salir = Button(frame_principal,text="Salir", command=salir)
bt_salir.config(bg = "#1e2329",fg="white", font=("Courier", 9, "italic"))
bt_salir.place(x=455, y=620, width=150, height=50)





ventana_principal.mainloop()