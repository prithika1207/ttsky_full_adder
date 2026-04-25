<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works
# Full Adder (TinyTapeout)

## 🧠 What it does
This project is a **1-bit full adder**.  
It adds three input bits and gives a sum and carry output.

---

## ⚙️ Inputs
- ui_in[0] = A  
- ui_in[1] = B  
- ui_in[2] = Carry-in (Cin)

---

## 📤 Outputs
- uo_out[0] = Sum  
- uo_out[1] = Carry  
- uo_out[7:2] = 0 (not used)

---

## 🧮 Working
It performs:

- Sum = A XOR B XOR Cin  
- Carry = (A&B) OR (B&Cin) OR (A&Cin)

---

## 🚀 Simple idea
It adds 3 bits and outputs a 2-bit result (sum and carry).

## How to test
## 🧪 How to Test

This design is tested using cocotb simulation.

- Apply inputs A, B, Cin
- Wait for output
- Check Sum and Carry result

### Example:
A = 1, B = 1, Cin = 0  
Output → Sum = 0, Carry = 1

All input combinations are tested automatically.

## External hardware

No external hardwares used
