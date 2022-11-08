## Char_PMOS_Vth_kp

The tool for finding the threshold voltage (V_th) and the transconductance (k_p) of a PMOS. (The k_p found does not account for the Early effect, so if you want it to be more accurate, the k_n must be divided by (1 + lambda*V_ds) where lambda = 1/V_A.)

You can run the only single python code to automate this. You don't need to edit nor open LTSpice files.

The code generates output as a text response. (No file is generated.)