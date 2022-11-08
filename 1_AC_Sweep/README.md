# 1_AC_Sweep

This tool evaluates the DC gain, crossover frequency and phase margin of an op-amp open-loop gain at various input and output DC voltage with variation of supply voltage, temperature and process corner of CMOS.

The simulation needs to be conducted as follow:

- on each 3 process corners (FF, TT, SS).
- each corner on 1.1 V or 1.8 V single power supply.
- 1.1 V supply voltage case:
    - varying input: 0.1, 0.3, 0.5, 0.7, 0.9 V 
    - varying output: 0.1, 0.55, 1.0 V (fix V_in at 0.55 V.)
- 1.8 V supply voltage case:
    - varying input: 0.1, 0.4, 0.7, 1.0, 1.3, 1.6 V
    - varying output: 0.1, 0.5, 0.9, 1.3, 1.7 V (fix V_in at 0.9 V.)
- each experiment is tested on 0, 35, 70 degree Celsius.

Thus, there are 171 experiments to run.

The output csv files will contain DC gain, crossover frequency and phase margin of an op-amp open-loop gain at various input and output DC voltage. The file names are indicated by:

`SIM_ac_sweep_{Vin/Vout}_{corner}_{Vsupply}_{Vin_value/Vout_value}_{temp}`

Where

- Vin/Vout: indicates whether Vin or Vout is a variated parameter. 
- corner: process corner (SS, TT, FF.)
- Vsupply: supply voltage (1.1 V or 1.8 V.)
- Vin_value/Vout_value: The value of V_in or V_out in that experiment. Depend on which is a variated parameter in that experiment.
- temp: temperature in Celsius.

The csv rows and columns will be arranged like this:

- The first, second and third columns indicate 0, 35, 70 degree Celsius respectively.
- The rows represent varying Vin/Vout voltages, from low to high. The variation will be like this:
    - 1.1 V supply voltage case:
        - varying input: 0.1, 0.3, 0.5, 0.7, 0.9 V 
        - varying output: 0.1, 0.55, 1.0 V (fix V_in at 0.55 V.)
    - 1.8 V supply voltage case:
        - varying input: 0.1, 0.4, 0.7, 1.0, 1.3, 1.6 V
        - varying output: 0.1, 0.5, 0.9, 1.3, 1.7 V (fix V_in at 0.9 V.)


