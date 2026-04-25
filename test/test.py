import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_fulladder(dut):
    dut._log.info("Starting Full Adder Test")

    # reset
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0

    await Timer(50, unit="ns")
    dut.rst_n.value = 1
    await Timer(50, unit="ns")

    test_cases = [
        (0,0,0,0,0),
        (0,0,1,1,0),
        (0,1,0,1,0),
        (0,1,1,0,1),
        (1,0,0,1,0),
        (1,0,1,0,1),
        (1,1,0,0,1),
        (1,1,1,1,1),
    ]

    for a, b, cin, exp_sum, exp_carry in test_cases:

        dut.ui_in.value = (cin << 2) | (b << 1) | a
        await Timer(20, unit="ns")

        out = int(dut.uo_out.value)

        actual_sum = out & 1
        actual_carry = (out >> 1) & 1

        assert actual_sum == exp_sum, f"SUM FAIL a={a} b={b} cin={cin}"
        assert actual_carry == exp_carry, f"CARRY FAIL a={a} b={b} cin={cin}"

        dut._log.info(
            f"PASS a={a} b={b} cin={cin} -> sum={actual_sum}, carry={actual_carry}"
        )
