# symulacja-orzel-reszka-dynamic-mati

Projekt dotyczy losowego przestawiania żetonów ułożonych na prostokątnej planszy o wymiarach m wierzy i n kolumny wg. zadanego algorytmu

![image](https://user-images.githubusercontent.com/31622223/215338044-42164a17-a00b-4744-9f99-75b0fe9f3686.png)

Rys. 1: Początkowe ustawienie żetonów

Algorytm przestawiania żetonów:

a.Początkowe ustawienie żetonów jest takie, że w pierwszych dwóch kolumnach znajdują się żetony żółte (1, orzeł, itp.), a w pozostałych żetony niebieskie (0, reszka); b.Dla każdego żetonu losowana jest liczba z przedziału od 1 do 4;

c.Kolejno każdy z żetonów zamieniany jest miejscami z żetonem znajdującym się w tym samym wierszu, w kolumnie o numerze wylosowanym w punkcie b.

d.Po dokonaniu zamiany wszystkich żetonów operacje b-c są powtarzane jeszcze czterokrotnie.
