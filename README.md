# LTSpice_with_Python :zap:
LTSpice with hand calculations is not enough, so Python comes to the rescue! [Link to the repository.](https://github.com/nutchanonj/LTSpice_with_Python)

NOTE: This repository's author gratefully wants to thank [Nuno Brum](https://github.com/nunobrum) for his [PyLTSpice](https://github.com/nunobrum/PyLTSpice) library. Without his great work, this project would not have been possible.

## Char_NMOS/PMOS_Vth_kn

The tool for finding the threshold voltage (V_th) and the transconductance (k_n) of an NMOS/PMOS. (The k_n found does not account for the Early effect, so if you want it to be more accurate, the k_n must be divided by (1 + lambda*V_ds) where lambda = 1/V_A.) [Link.](https://github.com/nutchanonj/LTSpice_with_Python/tree/main/Char_NMOS_Vth_kn)

## Char_NMOS/PMOS_VA

The tool for finding the Early voltage (V_A) of an NMOS/PMOS. [Link.](https://github.com/nutchanonj/LTSpice_with_Python/tree/main/Char_NMOS_VA)

## 1_AC_Sweep

This tool evaluates the DC gain, crossover frequency, and phase margin of an op-amp open-loop gain at various input and output DC voltages with variation of supply voltage, temperature, and process corner of CMOS. [Link.](https://github.com/nutchanonj/LTSpice_with_Python/tree/main/1_AC_Sweep)

## 2_Power

This tool evaluates the power usage of an op-amp. [Link.](https://github.com/nutchanonj/LTSpice_with_Python/tree/main/2_Power)

## 3_Noise

This tool evaluates the input-referred noise of an op-amp. [Link.](https://github.com/nutchanonj/LTSpice_with_Python/tree/main/3_Noise)

## 4_Settling_Time

This tool evaluates the settling time of a closed-loop op-amp when the step input is 0.5 V. [Link.](https://github.com/nutchanonj/LTSpice_with_Python/tree/main/4_Settling_Time)

## 5_Fourier

This tool evaluates the total harmonic distortion of an output wave when its swing is maximized to (V_DD - 0.2) V. The input frequency is 1 kHz, and evaluation time is 10 ms. [Link.](https://github.com/nutchanonj/LTSpice_with_Python/tree/main/5_Fourier)
