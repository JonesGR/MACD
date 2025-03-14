# MACD w Pythonie

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

## Wyniki
- Skrypt generuje trzy wykresy wizualizujące ruch cen i sygnały MACD.
- Wypisuje końcowy kapitał po zakończeniu symulowanej sesji handlowej.
- W pliku MACD.pdf znajduje się analiza wskaźnika MACD na podstawie danych uzyskanych z programu.


