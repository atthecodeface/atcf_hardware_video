# atcf_hardware_video

This repository contains the ATCF video timing and framebuffer CDL modules.

These modules support VGA, SVGA, LCD panels, and HDMI output (as in,
they have been used for all of these in real-world FPGAs).

## Status

The repository is in use in grip repository for RISC-V systems.

# Framebuffers

A module is provided which provides framebuffer timing; this is a
run-time configurable module, with a CSR interface, which can be
programmed with display size (width and height), front and back
porches, and synchronization pulse lengths and polarities.

It provides the synchronization and display enable signals required by
monitors and LCD panels, as well as some data to provide a framebuffer
to deliver the correct pixel data (using pipelining as required).

# Teletext

A teletext decoder module is provided that utilizes a teletext
character RAM (or ROM) to decode characters using the standard. This
module was originally written as part of the BBC microcomputer
implementation, but it is very useful for simple computer displays.

A teletext framebuffer is supplied which uses the teletext module,
which can be used by simple microcomputers but is especially used by
debug framebuffers using the dprintf infrastructure in
atcf_hardware_utils; this provides (on FPGA boards with HDMI or VGA
output) real-time hardware debugging information (such as APB access
address and data display, clock period measurements, bus accesses,
instruction execution, register dumps, etc)


