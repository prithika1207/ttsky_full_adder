import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_fulladder(dut):
    dut._log.info("Starting Gate-Level Hardened Simulation...")

    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0

    await Timer(50, unit="ns")
    dut.rst_n.value = 1
    await Timer(50, unit="ns")

    test_cases = [
        (0,0,0,0,0),
        (1,1,0,0,1),
        (1,1,1,1,1),
        (1,0,0,1,0),
        (0,1,0,1,0),
    ]

    for a, b, c, e_sum, e_carry in test_cases:
        dut.ui_in.value = (c << 2) | (b << 1) | a
        await Timer(20, unit="ns")

        try:
            output_val = int(dut.uo_out.value)
            actual_sum = output_val & 1
            actual_carry = (output_val >> 1) & 1

            assert actual_sum == e_sum, f"Sum Error: A={a} B={b} C={c}"
            assert actual_carry == e_carry, f"Carry Error: A={a} B={b} C={c}"

            dut._log.info(
                f"Input: {a},{b},{c} -> Sum: {actual_sum}, Carry: {actual_carry} [PASS]"
            )

        except ValueError:
            dut._log.info(f"Logic error: uo_out is {str(dut.uo_out.value)}")
            raise
  
