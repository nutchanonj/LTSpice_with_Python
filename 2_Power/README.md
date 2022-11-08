## 2_Power

This tool evaluates power usage of an op-amp. 

You can run the only single python code to automate this. You don't need to edit nor open LTSpice files.

The simulation needs to be conducted as follow:
- on each 3 process corners (FF, TT, SS).
- each corner on 1.1 V or 1.8 V single power supply.
- each experiment is tested on 0, 35, 70 degree Celsius.

Thus, there are 18 experiments to run.

This is one csv file generated from the code. The value of power usage is uW. The rows and columns in it will be arranged like this:

- The first, second and third columns indicate "SS", "TT", "FF" process corners respectively.
- For the supply voltage:
    - Rows 1-3 represent 1.8 V supply voltage.
    - Rows 4-6 represent 1.1 V supply voltage.
- For the temperature:
    - Rows 1,4 represent 0 degree Celsius.
    - Rows 2,5 represent 35 degree Celsius.
    - Rows 3,6 represent 70 degree Celsius.