import matplotlib
import matplotlib.style as mplstyle
import matplotlib.pyplot as plot
import numpy as np
import math

mplstyle.use(['dark_background', 'ggplot'])

def graph(x, y):
    plot.axis(x)
    plot.plot(y)
    plot.show()

def is_number(user_input):
    try:
        val = int(user_input)
    except:
        return False

    return True

def is_float(user_input):
    try:
        val = float(user_input)
    except:
        return False

    return True

def parameter():
    banner = False
    print("Ingrese el valor inicial del rango de graficacion en x: ")
    while not(banner):
        ini = raw_input()
        if is_float(ini):
            banner = True
        else:
            print("Opcion no valida, ingrese un numero valido: ")
    else:
        print("Ingrese el valor final del rango de graficacion en x: ")
        banner = False
        while not(banner):
            end = raw_input()
            if is_float(end):
                    banner = True
            else:
                print("Opcion no valida, ingrese un numero valido: ")
        else:
            print("Ingrese el valor inicial del rango de graficacion en y: ")
            banner = False
            while not(banner):
                ini2 = raw_input()
                if is_float(end):
                        banner = True
                else:
                    print("Opcion no valida, ingrese un numero valido: ")
            else:
                print("Ingrese el valor final del rango de graficacion en y: ")
                banner = False
                while not(banner):
                    end2 = raw_input()
                    if is_float(end):
                            banner = True
                    else:
                        print("Opcion no valida, ingrese un numero valido: ")
                else:
                    return [float(ini), float(end), float(ini2), float(end2)]

def graph_const():
    x = parameter()
    print("Ingrese el valor de la constante a graficar:")
    banner = False
    while not(banner):
        y = raw_input()
        if (is_float(y)):
            y = np.array([float(y) for i in xrange(len(x)*10) ])
            banner = True
        else:
            print("Opcion no valida, ingrese un numero entero: ")
    else:
        graph(x,y)

def f(a,b,x):
    return a*x + b

def graph_line():
    print("Ingrese el rango inicial de la recta a graficar:")
    banner = False
    while not(banner):
        y = raw_input()
        if (is_float(y)):
            banner = True
        else:
            print("Opcion no valida, ingrese un numero entero: ")
    else:
        banner = False
        print("Ingrese el rango final de la recta a graficar:")
        while not(banner):
            z = raw_input()
            if (is_float(z)):
                banner = True
            else:
                print("Opcion no valida, ingrese un numero entero: ")
        else:
            banner = False
            print("Ingrese el valor a de la funcion a graficar: ")
            while not(banner):
                a = raw_input()
                if (is_float(a)):
                    banner = True
                else:
                    print("Opcion no valida, ingrese un numero entero: ")
            else:
                banner = False
                print("Ingrese el valor b de la recta a graficar:")
                while not(banner):
                    b = raw_input()
                    if (is_float(b)):
                        banner = True
                    else:
                        print("Opcion no valida, ingrese un numero entero: ")
                else:
                    c = np.arange(int(y),int(z))
                    f = []
                    g = []
                    for i in c:
                        f.append(i)
                        g.append((float(a)*i)+float(b))
                    plot.plot(f,g)
                    plot.show()

def graph_parab():
    print("Ingrese el rango inicial de la recta a graficar:")
    banner = False
    while not(banner):
        y = raw_input()
        if (is_float(y)):
            banner = True
        else:
            print("Opcion no valida, ingrese un numero entero: ")
    else:
        banner = False
        print("Ingrese el rango final de la recta a graficar:")
        while not(banner):
            z = raw_input()
            if (is_float(z)):
                banner = True
            else:
                print("Opcion no valida, ingrese un numero entero: ")
        else:
            banner = False
            print("Ingrese el valor a de la funcion a graficar: ")
            while not(banner):
                a = raw_input()
                if (is_float(a)):
                    banner = True
                else:
                    print("Opcion no valida, ingrese un numero entero: ")
            else:
                banner = False
                print("Ingrese el valor b de la recta a graficar:")
                while not(banner):
                    b = raw_input()
                    if (is_float(b)):
                        banner = True
                    else:
                        print("Opcion no valida, ingrese un numero entero: ")
                else:
                    banner = False
                    while not(banner):
                        d = raw_input()
                        if (is_float(d)):
                            banner = True
                        else:
                            print("Opcion no valida, ingrese un numero entero: ")
                    else:
                        c = np.arange(int(y),int(z))
                        f = []
                        g = []
                        for i in c:
                            f.append(i)
                            g.append((float(a)*i*i)+(float(b)*i)+float(d))
                        plot.plot(f,g)
                        plot.show()

def graph_cubic():
    parameter()
    print("Ingrese el valor de la constante a graficar:")
    banner = False
    while not(banner):
        y = raw_input()
        if (is_number(y)):
            banner = True
        else:
            print("Opcion no valida, ingrese un numero entero: ")
    # graph()

def graph_cuadratic():
    parameter()
    print("Ingrese el valor de la constante a graficar:")
    banner = False
    while not(banner):
        y = raw_input()
        if (is_number(y)):
            banner = True
        else:
            print("Opcion no valida, ingrese un numero entero: ")
    # graph()

def graph_sin():
    parameter()
    print("Ingrese el valor de la constante a graficar:")
    banner = False
    while not(banner):
        y = raw_input()
        if (is_number(y)):
            banner = True
        else:
            print("Opcion no valida, ingrese un numero entero: ")
    # graph()

def graph_sin_t():
    parameter()
    print("Ingrese el valor de la constante a graficar:")
    banner = False
    while not(banner):
        y = raw_input()
        if (is_number(y)):
            banner = True
        else:
            print("Opcion no valida, ingrese un numero entero: ")
    # graph()


def select_graph(i):
    if i == "1":
        graph_const()
    elif i == "2":
        graph_line()
    elif i == "3":
        graph_parab()
    elif i == "4":
        graph_cubic()
    elif i == "5":
        graph_cuadratic()
    elif i == "6":
        graph_sin()
    else:
        graph_sin_t()

def main():
    print("Funciones para graficar:\n 1)f(t) = a \n 2)f(t) = ax + b \n 3)f(t) = ax^2 + bx + c \n 4)f(t) = ax^3 + bx^2 + cx + d \n 5)f(t) = ax^4 + bx^3 + cx^2 + dx + e \n 6)f(t) = Asen(wt) \n 6)f(t) = Asen(wt) / wt \nIngrese el numero de la funcion que quiere graficar: ")
    banner = False

    while not(banner):
        val = raw_input()
        if (is_number(val)):
            value = int(val)
            if (value > 0 and value < 8):
                banner = True
            else:
                print("Opcion no valida, ingrese un numero correspondiente a la funciones mostradas: ")
        else:
            print("Opcion no valida, ingrese un numero correspondiente a la funciones mostradas: ")
    else:
        select_graph(val)


if __name__ == "__main__":
    main()

# A = 10
# xs = np.arange(-30,30,0.2)
# ys = A*np.sin(xs)/xs

# fig, ax = plot.subplots()
# ax.plot(xs, ys)

# plot.show()
# nombre = input()
# print(nombre)