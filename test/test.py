import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_fulladder(dut):
    dut._log.info("Starting Full Adder Test")

    # Initialize inputs
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0

    await Timer(50, unit="ns")
    dut.rst_n.value = 1
    await Timer(50, unit="ns")

    # Test cases: (a, b, cin, expected_sum, expected_carry)
    test_cases = [
        (0, 0, 0, 0, 0),
        (0, 0, 1, 1, 0),
        (0, 1, 0, 1, 0),
        (0, 1, 1, 0, 1),
        (1, 0, 0, 1, 0),
        (1, 0, 1, 0, 1),
        (1, 1, 0, 0, 1),
        (1, 1, 1, 1, 1),
    ]

    for a, b, cin, exp_sum, exp_carry in test_cases:

        # Apply inputs
        dut.ui_in.value = (cin << 2) | (b << 1) | a

        await Timer(20, unit="ns")

        # Read output
        output = int(dut.uo_out.value)

        actual_sum = output & 0x1
        actual_carry = (output >> 1) & 0x1

        # Check results
        assert actual_sum == exp_sum, f"SUM FAIL: a={a} b={b} cin={cin}"
        assert actual_carry == exp_carry, f"CARRY FAIL: a={a} b={b} cin={cin}"

        dut._log.info(
            f"PASS: a={a} b={b} cin={cin} -> sum={actual_sum}, carry={actual_carry}"
        )
