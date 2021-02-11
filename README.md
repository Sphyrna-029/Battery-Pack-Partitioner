# Battery-Pack-Partitioner
Algorithm to sort 18650 cells by mAh into matched cell groups.


## Example usage:
```
usage: main.py [-h] [-f FILE] [-p PARRALLEL]

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
  -f FILE, --file FILE  Input CSV file.
  -p PARRALLEL, --parrallel PARRALLEL
                        Number of parrallel packs in your battery.
```


## Example Output:

```
==================================
=========== Statistics ===========
==================================
Average Cell Capactiy: 1981mAh
Total Pack Capacity: 25753mAh
Pack Nominal Voltage: 11.1v


==================================
Group 0
Total mAh: 25920
Cells: [2950, 2200, 2091, 2031, 2029, 1950, 1909, 1879, 1867, 1850, 1765, 1700, 1699]
==================================

==================================
Group 1
Total mAh: 25920
Cells: [2950, 2099, 2091, 2083, 2029, 1987, 1909, 1901, 1867, 1776, 1765, 1764, 1699]
==================================

==================================
Group 2
Total mAh: 25420
Cells: [2200, 2200, 2099, 2083, 2031, 1987, 1950, 1901, 1879, 1850, 1776, 1764, 1700]
==================================
```
