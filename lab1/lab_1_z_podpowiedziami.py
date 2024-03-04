import numpy as np
import matplotlib.pyplot as plt

from data import get_data, inspect_data, split_data

data = get_data()
inspect_data(data)

train_data, test_data = split_data(data)

# Simple Linear Regression
# predict MPG (y, dependent variable) using Weight (x, independent variable) using closed-form solution
# y = theta_0 + theta_1 * x - we want to find theta_0 and theta_1 parameters that minimize the prediction error

# We can calculate the error using MSE metric:
# MSE = SUM (from i=1 to n) (actual_output - predicted_output) ** 2

# get the columns
y_train = train_data['MPG'].to_numpy()
x_train = train_data['Weight'].to_numpy()

y_test = test_data['MPG'].to_numpy()
x_test = test_data['Weight'].to_numpy()

# TODO: calculate closed-form solution
# // podpowiedz studenta //
#    na bazie wzoru z instrukcji (1.8) mozemy
#    utworzyc "macierz obserwacji"
#    aby to zrobic musimy dodac kolumne jedynek
#    do danych treningowych. dzieki temu
#    uzyskujemy macierz o wymiarach ([m] x [n + 1]),
#    gdzie m to liczba obserwacji a n to liczba cech.
#    polecam do tego uzyc funkcji np.ones oraz np.concatenate
#
#    nastepnie aplikujemy wzor (1.13), wykorzystujac
#    utworzona macierz. przypominam tutaj o funkcjach
#    w numpy takich jak np.matmul, np.linalg.inv, oraz
#    fakcie ze kazda macierz ma transpozycje dostepna
#    poprzez atrybut T
#
#    jednoczesnie polecam wszystkie te rzeczy utworzyc
#    w dedykowanych funkcjach (ten mysi sprzet pomoze nam potem),
#    i nie zapomniec zeby tutaj uzyc danych do trenowania
#    a nie testowych - testowe sluza jako swego rodzaju
#    weryfikacja, i nie mieszamy tych dwoch zbiorow ze soba,
#    inaczej nie jestesmy w stanie sprawdzic czy model
#    mozna generalizowac na pule danych wieksza od
#    zestawu treningowego
# // koniec podpowiedzi //
theta_best = [0, 0]

# TODO: calculate error
# // podpowiedz studenta //
#    znajac theta, mozemy "po prostu" (no wiecie,
#    latwo zauwazyc, amirite?) obliczyc blad przy
#    uzyciu wzoru (1.3) - nie zapomnijcie ze to
#    zabawne koleczko to NIE JEST dot product
#    a podstawienie do wzoru na fukncje liniowa
#    (y = ax + b). jesli theta na gorze wyszlo
#    wam tak samo jak mi, to (b) bedzie w theta[0]
#    a (a) bedzie w theta[1]
#
#    tutaj przypominam o fajnej zaleznosci numpy:
#    mnozenie macierzy przez skalar (np. 2) to po
#    prostu `macierz * 2` - dodawanie skalarow tez
#    bedzie dzialac na calej macierzy (badz wektorze)
#    numpy ma tez funkcje np.sum (sumowanie, duh) oraz
#    np.square (kwadrat) - moga tutaj pomoc
# //koniec podpowiedzi //

# plot the regression line
# // podpowiedz studenta //
#    tutaj *w teorii* powinnismy teraz
#    uzyskac ladny, piekny wykres w ktorym
#    oprocz punktow z danych testowych bedzie widoczna
#    ladna linia opisujaca, mniej wiecej, charakterystyke
#    wszystkich danych
#
#    czy zauwazyliscie ze dane ktore tutaj mamy to
#    spalanie paliwa roznych samochodow? MPG czyli
#    Miles Per Gallon to jedna z wielu danych na temat
#    samochodow ktore sa tutaj wykorzystywane. byloby
#    to calkiem ciekawe... GDYBY KTOS GDZIES TO OPISAL
#    ZAMIAST NAM TO RZUCAC TAK O BYLE ZEBY BYLO. c:
#
#    jesli cos tutaj nie dziala, to warto przejsc jeszcze 
#    raz przez wzory i upewnic sie ze wszystko dobrze spisalismy
#    ewentualnie, pomoc na Discordzie
# // koniec podpowiedzi //
x = np.linspace(min(x_test), max(x_test), 100)
y = float(theta_best[0]) + float(theta_best[1]) * x
plt.plot(x, y)
plt.scatter(x_test, y_test)
plt.xlabel('Weight')
plt.ylabel('MPG')
plt.show()

# TODO: standardization
# // podpowiedz studenta //
#    standaryzacja jest opisana nawet niezle w instrukcji,
#    najwazniejsze co tu mozecie chciec wiedziec to ze
#    numpy ma funkcje do calosci tego wzoru,
#    np.mean - srednia z populacji
#    np.std - odchylenie standardowe populacji
#    ponownie wykorzystujemy tu sztuczke ze dzialania mozemy zapisac
#    w sposob matematyczny czyli literalnie przepisac wzor (1.15),
#    aplikujac go do wszystkich danych, zarowno testowych, jak i treningowych
# // koniec podpowiedzi //

# TODO: calculate theta using Batch Gradient Descent
# // podpowiedz studenta //
#    tutaj sie zaczyna zabawa, chociaz nie ma tragedii...
#    ...pod warunkiem ze juz sie zrozumialo caly temat kek
#
#    najpierw chcemy zrobic sobie dowolna thete (np. 0, 0),
#    lub losowa (np. np.random.randn(2, 1) - co da nam losowe
#    wartosci miedzy 0 i 1), i zrobic (chyba tylko jedna???)
#    iteracje *SPADKU PO GRADIENCIE* (nazwa, moze sie wydawac
#    bezsensowna - jesli nie rozumiecie czmu, to odsylam nie
#    do wykladu a do filmu 3Blue1Brown:
#    https://www.youtube.com/watch?v=IHZwWFHWa-w&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi&index=2,
#    okolo trzeciej minuty. jednoczesnie polecam calosc
#    playlisty, bo jest pieknie wytlumaczone. chyba ze nie
#    lubicie jak was dupa piecze ze na PG niektore wyklady
#    nie sa prowadzone najlepiej.)
#
#    po zainicjalizowaniu tety, mozemy obliczyc gradienty
#    zgodnie ze wzorem (1.7), z czym juz nie powinniscie
#    miec problemu (jesli macie, to polecam Discord),
#    a nastepnie wzor (1.14), ktory da nam nowa thete 
# // koniec podpowiedzi //

# TODO: calculate error
# // podpowiedz studenta //
#    w tym miejscu przyda sie wam funkcja do liczenia kosztu MSE
#    opisana wczesniej - nie zartowalem kiedy mowilem ze sie przyda
#    bo tutaj dobrym pomyslem jest obliczenie bledu dla tety
#    poczatkowej, oraz tety po jednym spadku - blad powinien spasc
#    w zaleznosci od rozmiaru zmiennej learning_rate - mozecie
#    sie pobawic i zauwazyc ze jesli z nim przesadzicie to totalnie
#    przestrzelicie sie i traficie jeszcze dalej niz byliscie na poczatku
#    mozecie to zwizualizowac sobie jako znanie kierunku w ktorym chcecie
#    isc, ale wziecie zbyt duzego kroku w tym (dobrym) kierunku, przez
#    co blad jest jeszcze wiekszy. jesli krok byl maly (np. rekomendowane 0.1)
#    no to blad powinien byc mniejszy.
#
#    potem mozecie calosc wsadzic do petli, i wyswietlac sobie np. co
#    10 iteracji jak wyglada aktualne teta - powinna powoli sie zblizac
#    do czegos podobnego co na wykresie pierwszym
#
#    chociaz prawda jest taka ze nie wiem czy taki byl plan tych ludzi,
#    bo nie jest tu napisane absolutnie nic w tym temacie, wiec bardzo
#    milo. w razie pytan, ponownie bede na Discordzie chociaz szczerze to sam
#    nie wiem za duzo lmao. milej zabawy neuoranmi (swoimi i konkutera).
# // koniec podpowiedzi //

# plot the regression line
x = np.linspace(min(x_test), max(x_test), 100)
y = float(theta_best[0]) + float(theta_best[1]) * x
plt.plot(x, y)
plt.scatter(x_test, y_test)
plt.xlabel('Weight')
plt.ylabel('MPG')
plt.show()