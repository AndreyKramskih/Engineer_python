from math import log, exp
#Расчётные функции для определения относительной пропускной способности
#Линейная пропускная характеристика
def lin_flow_char (Kv0, h):
    return Kv0 + (1 - Kv0) * h
#Параболическая пропускная характеристика
def par_flow_char (Kv0, h):
    return Kv0 + (1 - Kv0) * h * h
#Равнопроцентная пропускная характеристика
def ep_flow_char (Kv0, h):
    return Kv0 ** (1 - h)

H = 1e5 #Па, напор насоса (падение давления на всём участке сети, при полностью открытом РК)
Q_max = 100 #м3/ч, объёмный расход при полностью открытом РК
dens = 998.2 #кг/м3, плотность воды при нормальном атмосферном давлении и t = 20 C
Kv0 = 1 / 50 #диапазон регулирования РК 50:1

import numpy as np # библиотека работы с массивами
a = np.array([0.02, 0.05, 0.1, 0.2, 0.4, 0.6, 1]) #массив значений авторитета РК для исследуемых случаев
funcs = [lin_flow_char, par_flow_char, ep_flow_char] #исследуемые пропускные характеристики
hs = np.linspace(0, 1, 51) #положение штока РК

funcs_count = len(funcs) #количество исследуемых типов пропускных характеристик
a_count = a.shape[0] #количество значений авторитетов РК
h_count = hs.shape[0] #количество положений штоков РК
Qs = np.zeros((funcs_count, h_count, a_count), dtype = float) # объявляем массив относительных расходов

from math import sqrt
for i in range(funcs_count):
    for j in range(a_count):
        dp_valve = a[j] * H
        dp_notvalve = H - dp_valve
        Kvs = Q_max * sqrt(100 * dens / dp_valve)
        R_notvalve = dp_notvalve / Q_max / Q_max
        for k in range(h_count):
            Kv = Kvs * funcs[i](Kv0, hs[k])
            R_valve = 100 * dens / Kv / Kv
            R = R_valve + R_notvalve
            Q = sqrt(H / R)
            Qs[i, k, j] = Q / Q_max
import matplotlib.pyplot as plt #библотека для построения графиков
plt.rcParams['figure.figsize'] = [5, 5]
plt.rcParams.update({'font.size': 8})

plt.subplot(2, 2, 1)
plt.plot(hs, Qs[0])
plt.title('Расходные характеристики при различных значениях\n\
авторитета РК с линейной пропускной характеристикой')
plt.xlabel('Положение штока РК')
plt.ylabel('$Q/Q_{max}$')
plt.legend(a)
plt.xlim (0,1); plt.ylim (0,1)
plt.grid()

plt.subplot(2, 2, 2)
plt.plot(hs, Qs[1])
plt.title('Расходные характеристики при различных значениях\n\
авторитета РК с параболической пропускной характеристикой')
plt.xlabel('Положение штока РК')
plt.ylabel('$Q/Q_{max}$')
plt.legend(a)
plt.xlim (0,1); plt.ylim (0,1)
plt.grid()

plt.subplot(2, 2, 3)
plt.plot(hs, Qs[2])
plt.title('Расходные характеристики при различных значениях\n\
авторитета РК с равнопроцентной пропускной характеристикой')
plt.xlabel('Положение штока РК')
plt.ylabel('$Q/Q_{max}$')
plt.legend(a)
plt.xlim (0,1); plt.ylim (0,1)
plt.grid()
plt.show()