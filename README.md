# Battery-Pack-Partitioner
Algorithm to sort 18650 cells by mAh into matched cell groups.


## Example usage:
```usage: main.py [-h] [-f FILE] [-p PARALLEL] [-i ITERATIONS] [--hist]

████████████████████████████████████
██                                ██
██  ████  ████  ████  ████  ████  ████
██  ████  ████  ████  ████  ████  ████
██  ████  ████  ████  ████  ████  ████
██  ████  ████  ████  ████  ████  ████
██  ████  ████  ████  ████  ████  ████
██                                ██
████████████████████████████████████
    - 18650 Cell Partitioner +

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Input CSV file
  -p PARALLEL, --parallel PARALLEL
                        Number of parallel packs in your battery
  -i ITERATIONS, --iterations ITERATIONS
                        Number of branch-&-bound iterations to optimize the result
  --hist                Display a histogram with capacity distribution at the end of the process
```


## Example Output:

```
$ python main.py -f example.csv -p 3

Stats:
  - Avg. Cell Capactiy:   1981 mAh
  - Tot. Pack Capacity:   25753 mAh
  - Pack Nominal Voltage: 11 V


Group #0 (tot. 25920 mAh)
  - Cell N° 17  -  2950 mAh
  - Cell N° 39  -  2200 mAh
  - Cell N° 26  -  2091 mAh
  - Cell N° 6   -  2031 mAh
  - Cell N° 32  -  2029 mAh
  - Cell N° 8   -  1950 mAh
  - Cell N° 24  -  1909 mAh
  - Cell N° 10  -  1879 mAh
  - Cell N° 18  -  1867 mAh
  - Cell N° 23  -  1850 mAh
  - Cell N° 34  -  1765 mAh
  - Cell N° 3   -  1700 mAh
  - Cell N° 16  -  1699 mAh

Group #1 (tot. 25920 mAh)
  - Cell N° 36  -  2950 mAh
  - Cell N° 1   -  2099 mAh
  - Cell N° 7   -  2091 mAh
  - Cell N° 31  -  2083 mAh
  - Cell N° 13  -  2029 mAh
  - Cell N° 33  -  1987 mAh
  - Cell N° 5   -  1909 mAh
  - Cell N° 30  -  1901 mAh
  - Cell N° 37  -  1867 mAh
  - Cell N° 19  -  1776 mAh
  - Cell N° 15  -  1765 mAh
  - Cell N° 28  -  1764 mAh
  - Cell N° 35  -  1699 mAh

Group #2 (tot. 25420 mAh)
  - Cell N° 2   -  2200 mAh
  - Cell N° 21  -  2200 mAh
  - Cell N° 20  -  2099 mAh
  - Cell N° 12  -  2083 mAh
  - Cell N° 25  -  2031 mAh
  - Cell N° 14  -  1987 mAh
  - Cell N° 27  -  1950 mAh
  - Cell N° 11  -  1901 mAh
  - Cell N° 29  -  1879 mAh
  - Cell N° 4   -  1850 mAh
  - Cell N° 38  -  1776 mAh
  - Cell N° 9   -  1764 mAh
  - Cell N° 22  -  1700 mAh
```
