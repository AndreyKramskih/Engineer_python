from math import log, exp
#Расчётные функции
#Линейная пропускная характеристика
def lin_flow_char (Kv0, h):
    return Kv0 + (1 - Kv0) * h
#Параболическая пропускная характеристика
def par_flow_char (Kv0, h):
    return Kv0 + (1 - Kv0) * h * h
#Равнопроцентная пропускная характеристика
def ep_flow_char (Kv0, h):
    return Kv0 ** (1 - h)

import numpy as np #библиотека для работы с массивами

N = 51 #Количество точек разбиения диапазона [0; 1] относительного положения штока h
hs = np.linspace(0, 1, N) #h - положение штока, s - означает, что это массив (множественное число)
#Массив размерностью [N, 4] для хранения значений относительных Kv для четырёх пропускных характеристик
#0 - линейная (Kv0 = 0,02,регулирующее отношение 50:1), 1 - парабалическая (Kv0 = 0,02),
#2 - равнопроцентная (Kv0 = 0,02), 3 - равнопроцентная (Kv0 = 0,01, регулирующее отношение 100:1)
legends = ['Линейная 50:1', 'Параболическая 50:1', 'Равнопроцентная 50:1', 'Равнопроцентная 100:1']
Kvs = np.zeros((hs.shape[0], len(legends)), dtype = float) #создаём массив из нулей
Kv0s = np.array([0.02, 0.02, 0.02, 0.01]) #значения относительных Kv0 для исследуемых 4-х характеристик
funcs = [lin_flow_char, par_flow_char, ep_flow_char, ep_flow_char] #список функций - проходных характеристик

#Формирование данных для графиков
for i in range(N):
    for j in range(len(funcs)):
        Kvs[i, j] = funcs[j](Kv0s[j], hs[i])

import matplotlib.pyplot as plt #библотека для построения графиков
plt.rcParams['figure.figsize'] = [10, 10]
plt.rcParams.update({'font.size': 16})
plt.plot(hs, Kvs)
plt.title('Пропускные характеристики')
plt.xlabel('Положение штока РК')
plt.ylabel('Относительный $K_v$')
plt.legend(legends)
plt.xlim (0,1); plt.ylim (0,1)
plt.grid()
plt.show()