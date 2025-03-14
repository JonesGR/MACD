# Strategia MACD w Pythonie

## Opis
Ten skrypt w języku Python analizuje dane finansowe przy użyciu wskaźnika MACD (Moving Average Convergence Divergence). Wczytuje ceny zamknięcia z pliku CSV, oblicza EMA (Eksponencjalna Średnia Ruchoma) i rysuje wykresy MACD wraz z sygnałami kupna i sprzedaży. Dodatkowo symuluje prostą strategię handlową w celu oceny rentowności.

## Funkcje
- Wczytuje ceny zamknięcia z pliku CSV.
- Oblicza Eksponencjalną Średnią Ruchomą (EMA) dla różnych okresów.
- Wylicza wartości MACD i linii sygnałowej.
- Rysuje wykresy cen zamknięcia, MACD i sygnałów transakcyjnych.
- Symuluje strategię handlową w celu określenia wzrostu kapitału.

## Wymagane biblioteki
Upewnij się, że masz zainstalowane następujące biblioteki Pythona:

```bash
pip install matplotlib
```

## Jak używać
1. Przygotuj plik CSV (`wig20_d.csv`) zawierający co najmniej jedną kolumnę `Close` z historycznymi cenami zamknięcia.
2. Uruchom skrypt:

```bash
python script.py
```

## Opis funkcji
### `calculate_EMA(sample, vector=[])`
Oblicza Eksponencjalną Średnią Ruchomą (EMA) dla określonego okresu.

### `draw_plot_1(close_prices=[], MACD=[], SIGNAL=[], buy_sell=False, start_i=-5, stop_i=1010, buys=[], sells=[])`
Rysuje główny wykres przedstawiający ceny zamknięcia i sygnały kupna/sprzedaży.

### `draw_plot_2(close_prices=[], MACD=[], SIGNAL=[], start_i=-5, stop_i=1010)`
Rysuje wykres MACD i linii sygnałowej wraz z sygnałami transakcyjnymi.

### `simulate(capital, start_i, end_i, close_prices=[], buys=[], sells=[])`
Symuluje prostą strategię handlową opartą na sygnałach MACD i zwraca końcowy kapitał.

## Przykładowe wyniki
- Skrypt generuje trzy wykresy wizualizujące ruch cen i sygnały MACD.
- Wypisuje końcowy kapitał po zakończeniu symulowanej sesji handlowej.

## Licencja
Ten projekt jest open-source i może być dowolnie modyfikowany.

