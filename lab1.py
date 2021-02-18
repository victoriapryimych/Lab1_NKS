import csv


def p_time(time, lam):
    h_time = int(time // h)
    s = 1
    for k in range(h_time):
        s -= fi[k] * h
    s -= fi[h_time] * (time - h * h_time)
    if lam == 1:
        return round(fi[h_time] / s, 6)
    return round(s, 6)


with open('input_v20.csv', newline='') as file:
    reader = csv.reader(file)
    t_input = list(reader)
t_vidm = []
for t in t_input:
    t_vidm.append(t[0])

t_vidm = list(map(int, t_vidm))
gamma = float(input("Введіть значення гамма: "))
time1 = int(input("Введіть час, для якого треба визначити ймовірність безвідмовної роботи: "))
time2 = int(input("Введіть час, для якого треба визначити інтенсивність відмов: "))
print("-------------------------------------------------------------------")
T_ser = sum(t_vidm) / len(t_vidm)
print("Середній наробіток до відмови:", T_ser)
t_vidm.sort()
h = max(t_vidm) / 10
intervals = []
for i in range(11):
    intervals.append(round(i * h, 6))
print("Інтервали:")
for i in range(10):
    print("Інтервал {}: {} - {}".format(i+1, intervals[i], intervals[i + 1]))

Ni = []
count = 0
for i in range(10):
    for j in t_vidm:
        if intervals[i] < j <= intervals[i + 1]:
            count += 1
    Ni.append(count)
    count = 0

fi = []
for n in Ni:
    fi.append(round(n / (len(t_vidm) * h), 6))
print("Значення статистичної щільності розподілу ймовірності відмови:")
for i in range(len(fi)):
    print("f{} = {:.6f}".format(i+1, fi[i]))

P = []
P0 = 1
P.append(P0)
S = 1
for f in fi:
    S -= f * h
    P.append(round(S, 2))
print("Ймовірність безвідмовної роботи пристрою на час правої границі інтервалу:")
print("P(0) = {}".format(P[0]))
for i in range(len(P)-1):
    print("P({}) = {:.3f}".format(intervals[i+1], P[i+1]))

T_gamma = 0
for i in range(len(P) - 1):
    if P[i] > gamma > P[i + 1]:
        d = round((P[i] - gamma) / (P[i] - P[i + 1]), 2)
        T_gamma = i + h * d
print("Статистичний γ-відсотковий наробіток на відмову:\nT_gamma:", T_gamma)

print("Ймовірність безвідмовної роботи на час {} годин:\nP({}) = {}".format(time1, time1, p_time(time1, 0)))
print("Інтенсивність відмов на час {} годин:\nlambda({}) = {}".format(time2, time2, p_time(time2, 1)))
