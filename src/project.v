/*
 * Copyright (c) 2024 Your Name
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_full_adder (
    input  wire [7:0] ui_in,
    output wire [7:0] uo_out,
    input  wire [7:0] uio_in,
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    input  wire       ena,
    input  wire       clk,
    input  wire       rst_n
);

    wire a   = ui_in[0];
    wire b   = ui_in[1];
    wire cin = ui_in[2];

    // ✅ Correct output assignment
    assign {uo_out[1], uo_out[0]} = a + b + cin;

    assign uo_out[7:2] = 6'b000000;
    assign uio_out = 8'b00000000;
    assign uio_oe  = 8'b00000000;

    // Prevent unused warnings
    wire _unused = &{ena, clk, rst_n, uio_in};

endmodule
