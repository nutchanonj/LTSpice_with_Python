# 1_AC_Sweep

This tool evaluates the DC gain, crossover frequency and phase margin of an op-amp open-loop gain at various input and output DC voltage with variation of supply voltage, temperature and process corner of CMOS.

The simulation needs to be conducted as follow:

- on each 3 process corners (FF, TT, SS).
- each corner on 1.1 V or 1.8 V single power supply.
- 1.1 V case:
    - varying input: 0.1, 0.3, 0.5, 0.7, 0.9 V
    - varying output: 0.1, 0.55, 1.0 V
- 1.8 V case:
    - varying input: 0.1, 0.4, 0.7, 1.0, 1.3, 1.6 V
    - varying output: 0.1, 0.5, 0.9, 1.3, 1.7 V
- each experiment is tested on 0, 35, 70 \si{\degreeCelsius}.

Thus, there are 171 experiments to run.

