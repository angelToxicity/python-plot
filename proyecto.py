import matplotlib
import matplotlib.style as mplstyle
import matplotlib.pyplot as plot
import numpy as np
import math
import sympy.integrals


def cond_ini(param):
    cont = 0
    t = np.zeros((3,1))

    if param == "x":
        print("Ingrese las condiciones iniciales de los tanques X(0): ")
    else:
        print("Ingrese las condiciones iniciales de las entradas u(0): ")
    
    while (cont < 3):
        inp = input()
        t[cont] = is_number(inp)
        cont = cont + 1
    return t

def statement(i, object):
    if i == "1":
        state = "primer"
    elif i == "2":
        state = "segundo"
    elif i == "3":
        state = "tercer"
    
    if object == "valvula":
        print("Ingrese el valor (R"+i+") de la valvula: ")
    elif object == "capac":
        print("Ingrese la capacitancia (C"+i+") del "+state+" tanque: ")
    elif object == "tanque":
        print("Ingrese la altura maxima (h"+i+") del "+state+" tanque: ")

    val = input()
    value = is_number(val)
    if value != Exception:
        return value
    
def e_matrix(I,A,param):
    return I + A*param + ((A@A)*(param**2))/2 + ((A@A@A)*(param**3))/6 + ((A@A@A@A)*(param**4))/24

def is_number(user_input):
    try:
        val = float(user_input)
        if val >= 0:
            return val
        else:
            raise Exception
    except:
        print("Opcion no valida, ingrese un numero valido: ")
        inp = input()
        is_number(inp)

def graph(x1, x2, x3, y):
    #Grafica de variable de estado x1
    plot.figure(1)
    ax_f = plot.subplot()
    ax_f.set_title('Variables de estado')
    plot.plot(y, x1, label="x1(t)")
    plot.legend()

    #Grafica de variable de estado x2
    plot.figure(2)
    ay_f = plot.subplot()
    ay_f.set_title('Variables de estado')
    plot.plot(y, x2, label="x2(t)")
    plot.legend()

    #Grafica de variable de estado x3
    plot.figure(3)
    az_f = plot.subplot()
    az_f.set_title('Variables de estado')
    plot.plot(y, x3, label="x3(t)")
    plot.legend()

    plot.show()

def main():
    print("Bienvenido al sistema de analisis para el llenado y vaciado de tanques en serie: \nLas consideraciones de este software es que evaluaremos la respuesta del sistema para una entrada de tipo impulso unitario u(t)\n")
    h1 = statement("1", "tanque")
    h2 = statement("2", "tanque")
    h3 = statement("3", "tanque")
    C1 = statement("1", "capac")
    C2 = statement("2", "capac")
    C3 = statement("3", "capac")
    R1 = statement("1", "valvula")
    R2 = statement("2", "valvula")
    R3 = statement("3", "valvula")
    print("Ingrese el tiempo t en segundos, para el cual analizar el sistema: ")
    inp = input()
    t = is_number(inp)
    print("Ingrese el numero de veces a realizar el ciclo para analisis del sistema: ")
    inp = input()
    t_exe = 1/is_number(inp)
    x_0 = cond_ini("x").reshape(3,1)
    u_0 = cond_ini("u").reshape(3,1)
    u = np.ones((3,1))
    x1_plot = []
    x2_plot = []
    x3_plot = []
    x1_plot.append(x_0[0])
    x2_plot.append(x_0[1])
    x3_plot.append(x_0[2])
    # Creamos la matriz A
    A = np.array([(-1/(R1*C1),1/(R1*C1),0),(1/(R1*C2),(-1/C2)*(1/R1+1/R2),0),(0,1/(R2*C3),-1/(R3*C3))]).reshape(3,3)

    # Creamos la matriz B de u(t)
    B = np.array([(1/C1,0,0),(0,1/C2,0),(0,0,1/C3)]).reshape(3,3)

    # Creamos la matriz identidad I
    I = np.array([(1,0,0),(0,1,0),(0,0,1)]).reshape(3,3)

    for z in np.arange(1.0,t+1.0,t_exe):
        # Creamos la matriz exponencial e^At
        e = e_matrix(I,A,z)
        e.reshape((3,3))

        # Resolvemos X(t)
        w = np.zeros((3,1))

        #Sumatoria del metodo de integracion
        for i in range(1,100):
            w += e_matrix(I,A,z-((z*i)/100)) @ B @ u
        
        #Completar operaciones del metodo numerico
        integral = (z/100)*(((e@B@u_0 + I@B@u)/2) + w)
        x = (e @ x_0) + integral

        x1 = np.array((1,0,0)) @ x
        x2 = np.array((0,1,0)) @ x
        x3 = np.array((0,0,1)) @ x
        x1_plot.append(x1)
        x2_plot.append(x2)
        x3_plot.append(x3)
    y = np.arange(0,t,t/len(x1_plot))

    if x1 > h1:
        print("Se supera la altura maxima del tanque 1. Revise los datos e intente nuevamente")
    elif x2 > h2:
        print("Se supera la altura maxima del tanque 2. Revise los datos e intente nuevamente")
    elif x3 > h3:
        print("Se supera la altura maxima del tanque 3. Revise los datos e intente nuevamente")
    elif x1 < 0 or x2 < 0 or x2 < 0:
        print("Los datos generan resultados incorrectos. Revise los datos e intente nuevamente")
    else:
        graph(x1_plot, x2_plot, x3_plot, y)

if __name__ == "__main__":
    main()