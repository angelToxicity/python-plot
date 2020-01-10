import matplotlib
import matplotlib.style as mplstyle
import matplotlib.pyplot as plot
import numpy as np
import math

mplstyle.use(['dark_background', 'ggplot'])

def plot_function(x,y,type):
    if type == 'linear':
        f = []
        g = []
        for i in y:
            f.append(i)
            if len(x) == 2:
                g.append((x[0]*i)+x[1])
            elif len(x) == 3:
                g.append((x[0]*i*i)+(x[1]*i)+x[2])
            elif len(x) == 4:
                g.append((x[0]*i*i*i)+(x[1]*i*i)+(x[2]*i)+x[3])
            elif len(x) == 5:
                g.append((x[0]*i*i*i*i)+(x[1]*i*i*i)+(x[2]*i*i)+(x[3]*i)+x[4])
        plot.plot(f,g)
    else:
        plot.plot(x,y)

    plot.show()

def is_number(user_input):
    try:
        val = int(user_input)
        return val
    except:
        print("Opcion no valida, ingrese un numero valido: ")
        input = raw_input()
        is_number(input)

def is_float(user_input):
    try:
        val = float(user_input)
        return val
    except:
        print("Opcion no valida, ingrese un numero valido: ")
        input = raw_input()
        is_float(input)

def parameter():
    print("Ingrese el valor inicial del rango de graficacion en x: ")
    ini = raw_input()
    ini = is_float(ini)
    print("Ingrese el valor final del rango de graficacion en x: ")
    end = raw_input()
    end = is_float(end) + 1
    print("Ingrese el valor inicial del rango de graficacion en y: ")
    ini2 = raw_input()
    ini2 = is_float(ini2)
    print("Ingrese el valor final del rango de graficacion en y: ")
    end2 = raw_input()
    end2 = is_float(end2)
    return [ini, end, ini2, end2]

def graph_const():
    x = parameter()
    print("Ingrese el valor de la constante a graficar:")
    y = raw_input()
    y = is_float(y)
    y = np.array([y for i in xrange(len(x)*10) ])
    plot.axis(x)
    plot.plot(y)
    plot.show()

def graph_line():
    print("Ingrese el rango inicial de la recta a graficar:")
    y = raw_input()
    y = is_float(y)
    print("Ingrese el rango final de la recta a graficar:")
    z = raw_input()
    z = is_float(z) + 1
    print("Ingrese el valor a de la funcion a graficar: ")
    a = raw_input()
    a = is_float(a)
    print("Ingrese el valor b de la recta a graficar:")
    b = raw_input()
    b = is_float(b)
    c = np.arange(y,z)
    plot_function([a,b],c,'linear')

def graph_parab():
    print("Ingrese el rango inicial de la funcion a graficar:")
    y = raw_input()
    y = is_float(y)
    print("Ingrese el rango final de la funcion a graficar:")
    z = raw_input()
    z = is_float(z)
    print("Ingrese el valor a de la funcion a graficar: ")
    a = raw_input()
    a = is_float(a)
    print("Ingrese el valor b de la funcion a graficar:")
    b = raw_input()
    b = is_float(b)
    print("Ingrese el valor c de la funcion a graficar:")
    d = raw_input()
    d = is_float(d)
    c = np.arange(y,z)
    plot_function([a,b,d],c,'linear')

def graph_cubic():
    print("Ingrese el rango inicial de la funcion a graficar:")
    y = raw_input()
    y = is_float(y)
    print("Ingrese el rango final de la funcion a graficar:")
    z = raw_input()
    z = is_float(z) + 1
    print("Ingrese el valor a de la funcion a graficar: ")
    a = raw_input()
    a = is_float(a)
    print("Ingrese el valor b de la funcion a graficar:")
    b = raw_input()
    b = is_float(b)
    print("Ingrese el valor c de la funcion a graficar:")
    d = raw_input()
    d = is_float(d)
    print("Ingrese el valor d de la funcion a graficar:")
    e = raw_input()
    e = is_float(e)
    c = np.arange(y,z)
    plot_function([a,b,d,e],c,'linear')

def graph_cuadratic():
    print("Ingrese el rango inicial de la funcion a graficar:")
    y = raw_input()
    y = is_float(y)
    print("Ingrese el rango final de la funcion a graficar:")
    z = raw_input()
    z = is_float(z) + 1
    print("Ingrese el valor a de la funcion a graficar: ")
    a = raw_input()
    a = is_float(a)
    print("Ingrese el valor b de la funcion a graficar:")
    b = raw_input()
    b = is_float(b)
    print("Ingrese el valor c de la funcion a graficar:")
    d = raw_input()
    d = is_float(d)
    print("Ingrese el valor d de la funcion a graficar:")
    e = raw_input()
    e = is_float(e)
    print("Ingrese el valor e de la funcion a graficar:")
    h = raw_input()
    h = is_float(h)
    c = np.arange(y,z)
    plot_function([a,b,d,e,h],c,'linear')

def graph_sin():
    print("Ingrese el rango inicial de la funcion a graficar:")
    y = raw_input()
    y = is_float(y)
    print("Ingrese el rango final de la funcion a graficar:")
    z = raw_input()
    z = is_float(z)
    print("Ingrese el valor A de la funcion a graficar: ")
    a = raw_input()
    a = is_float(a)
    c = np.arange(y,z,0.2)
    g = a*np.sin(c)
    plot_function(c,g,'sin')

def graph_sin_t():
    print("Ingrese el rango inicial de la funcion a graficar:")
    y = raw_input()
    y = is_float(y)
    print("Ingrese el rango final de la funcion a graficar:")
    z = raw_input()
    z = is_float(z)
    print("Ingrese el valor A de la funcion a graficar: ")
    a = raw_input()
    a = is_float(a)
    c = np.arange(y,z,0.2)
    g = (a*np.sin(c))/c
    plot_function(c,g,'sin')

def select_graph(i):
    if i == 1:
        graph_const()
    elif i == 2:
        graph_line()
    elif i == 3:
        graph_parab()
    elif i == 4:
        graph_cubic()
    elif i == 5:
        graph_cuadratic()
    elif i == 6:
        graph_sin()
    else:
        graph_sin_t()

def main():
    print("Funciones para graficar:\n 1)f(t) = a \n 2)f(t) = ax + b \n 3)f(t) = ax^2 + bx + c \n 4)f(t) = ax^3 + bx^2 + cx + d \n 5)f(t) = ax^4 + bx^3 + cx^2 + dx + e \n 6)f(t) = Asen(wt) \n 7)f(t) = Asen(wt) / wt \nIngrese el numero de la funcion que quiere graficar: ")
    val = raw_input()
    value = is_number(val)
    if (value > 0 and value < 8):
        select_graph(value)

if __name__ == "__main__":
    main()