from controlvalve import ControlValve

Q = 100  # номинальный расход рабочей среды через рассматриваемый участок, м3/ч
dp = 1e5 # потери давления на рассматриваем участке (Па) при расходе Q без учёта
         # нивелирной составляющей и падении давления на РК

#Примем следующие параметры РК:
#диапазон регулирования 50 Фо=0,02
#расход Q через РК должен наблюдаться при положении штока h=0,9
#авторитет РК при относительном положении штока h=0,9 и авторитете m=0,1

F0 = 1 /50; h0 = 0.9; m = 0.1

#С помощью статического метода ControlValve.Kv_from_m_dp_Q найдем значение Kv
#при котором при заданных условиях расход через РК будет равен Q при авторитете РК m
help(ControlValve.Kv_from_m_dp_Q)
Kv = ControlValve.Kv_from_m_dp_Q(m, dp, Q)
print(Kv) #м3/ч
# Если бы h0=1 то на этом можно было бы и остановиться, выбрав РК с Kvs выше найденного Kv
#Но в нашем случае условия заданы для h0=0,9 В этом случае следует использовать статический метод
#ControlValve.Kvs_from_m_dp_Q_h
#Найдём требуемое значение Kvs РК для заданных условий для всех трёх видов пропускной характеристики.
help(ControlValve.Kvs_from_m_dp_Q_h)

Kvss = []
Kvss.append(ControlValve.Kvs_from_m_dp_Q_h(m, dp, Q, h0, 0, F0))
Kvss.append(ControlValve.Kvs_from_m_dp_Q_h(m, dp, Q, h0, 1, F0))
Kvss.append(ControlValve.Kvs_from_m_dp_Q_h(m, dp, Q, h0, 2, F0))
print(Kvss)

#Из результатов расчёта видно, что для достижения заданного условия - расход Q и авторитет РК m=0,1
# при h=h0  РК с различными видами пропускных характеристик должны иметь различные значения Kvs

# Создаём объекты класса ControlValve с различными пропускными характеристиками
# расходная характеристика которых проходит через точку (h = 0,9; Q = 100)
cvs = [ControlValve(Kv, 0, F0, h0), ControlValve(Kv, 1, F0, h0), ControlValve(Kv, 2, F0, h0)]
titles = ["Линейная", "Равнопроцентная", "Параболическая"]
import matplotlib.pyplot as plt
plt.rcParams['font.size'] = 12.0
fig, ax = plt.subplots(figsize = (10,5))
ax.set_title("Расходные характеристики РК с различными видами пропускных\nхарактеристик"
            " при заданной режимной точке ($\overline{h}_0 =$" + f"{h0}" + f", Q={Q}" + " $м^3/ч$)")
ax.grid(); ax.set_xlim(0,1); ax.set_ylim(0,105 )
for i, cv in enumerate(cvs):
    hs, Qs, _ = cv.get_char(Q, m, h0)
    ax.plot(hs, Qs, label = titles[i])
ax.set_xlabel('$\overline{h}$'); ax.set_ylabel('$Q,\ м^3/ч$')
ax.legend()

import matplotlib.pyplot as plt
plt.rcParams['font.size'] = 12.0
fig, ax = plt.subplots(figsize = (10,5))
ax.set_title("Пропускные характеристики РК")
ax.grid(); ax.set_xlim(0,1); ax.set_ylim(0,max(Kvss))
for i, cv in enumerate(cvs):
    hs, Qs, _ = cv.get_char(Kv, 1, h0)
    ax.plot(hs, Qs, label = titles[i])
ax.set_xlabel('$\overline{h}$'); ax.set_ylabel('$K_V,\ м^3/ч$')
ax.legend();

plt.show()
#Kvs РК с линейной, равнопроцентной и параболической пропускными характеристиками
print(cvs[0].Kvs, cvs[1].Kvs, cvs[2].Kvs)
# Полный перечень методов класса ControlValve
help(ControlValve)

