from minimoscuadrados import linealizacion
import matplotlib.pyplot as plt
import random

voltaje = [[0.74	, 1.03	, 1.45	, 1.65	, 2.03	, 2.20	, 2.53	, 2.85	, 3.20	, 3.54	], #R1
           [0.47	, 0.58	, 0.77	, 0.99	, 1.2	, 1.36	, 1.59	,1.71	], #R2
           [0.22	, 0.30	, 0.42	, 0.54	, 0.63	, 0.70	, 0.83	, 0.96	, 1.04	, 1.12	], #R3
           [1.56, 2.28, 2.57, 3.58, 3.81, 4.59, 5.25, 6.01, 6.55 , 7.09], #Serie
           [0.10, 0.17, 0.22, 0.29, 0.35, 0.41, 0.43, 0.51, 0.53,0.62] #Paralelo
           ]
deltax = 0.01
deltay = 0.01
def generar_color_aleatorio():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_hex = "#{:02X}{:02X}{:02X}".format(r, g, b)

    return color_hex
valor = []
nombre = [ "R1" , "R2" , "R3" , "Serie" , "Paralelo"]
for i in range(5):
    intensidad = [0.02	, 0.03	, 0.04	, 0.05	, 0.06	, 0.07	, 0.08	, 0.09	, 0.10	, 0.11	] #Eje x
    valor.append( linealizacion(intensidad , voltaje[i] , deltax , deltay))
    print(valor[i].linea(),"\n", valor[i].ejex() ,"\n", valor[i].ejey())
    print(valor[i].incertidumbre())
    color1 = generar_color_aleatorio()
    color2 = generar_color_aleatorio()
    plt.grid(True)
    plt.xlabel("Intensidad (A)")
    plt.ylabel("Voltaje (V)")
    plt.title("Voltaje vs Intensidad, " + nombre[i])
    plt.scatter(intensidad, voltaje[i][:len(intensidad)], color=color1, label="Datos Experimentales")
    plt.plot(intensidad, voltaje[i][:len(intensidad)], color=color1)
    plt.plot(intensidad, valor[i].ajuste(), color=color2, linestyle="--", label="Ajuste Lineal")
    plt.legend()
    plt.show()
    

