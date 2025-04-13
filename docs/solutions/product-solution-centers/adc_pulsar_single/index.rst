Single-Channel, SPI-interface SAR ADC Developer Resources
#########################################################

.. attention::

   This is a draft, very much WIP document in a fork of `<https://github.com/analogdevicesinc/documentation>`__

Family Overview
================

This page describes various hardware and software resources available for evaluating and developing with certain Analog Devices' single-channel, SPI-interface, successive-approximation (SAR) Analog to Digital Converters. Not all such devices across ADI's product line are covered here, however the devices on this page are all supported by the same Linux or no-OS (bare metal) device driver, and FPGA HDL IP core and project.

The evaluation and development boards across these devices use several industry-standard and ADI-proprietary connectors, compatible with industry-standard and proprietary carrier (processor/FPGA) boards. The choice depends on the developer's needs; If the development flow involves software and HDL development on standard carrier boards, it is best to use either the Pmod or FMC boards. Review the example projects and their user guides for the various options in order to make the best choice.

Wherever possible, pre-built programming and boot files are provided for the various carrier / eval board combinations. These typically implement an IIO (Industrial Input-Output) server, compatible with a wide array of software tools and language bindings, easing development considerably.

Getting Started
===============

There are several combinations of evaluation and development boards and controller platforms, with different capabilities and associated software and device driver resources. Review the options and choose the one that best suits your needs. In general combinations fall into two categories: 

Legacy evaluation boards and software are geared toward performance evaluation, with Windows-based GUI software that computes typical metrics such as THD, SNR, linearity, etc. These are closed-source, and further development requires moving to other controller boards and software development environments. Examples for this famly of ADCs are shown in :numref:`fig-adi_systems`. The FMC eval boards can target either the SDP-H1 board or standard development platforms, while the SDP eval boards can only target the SDP-B or SDP-H1 board.

.. _fig-adi_systems:

.. figure:: ADI_systems_block_diags.png
   :align: center
   :width: 600px
   
   ADI Proprietary Evaluation Systems

The second category of development systems is based on commercially available development platforms running open-source software, firmware, and HDL. Examples for this family of ADCs are shown in :numref:`fig-iio_systems`. These systems are based on the Linux Industrial Input/Output (IIO) framework and are much more flexible, with multiple cross-platform options for both evaluation software and development software.

.. _fig-iio_systems:

.. figure:: iio_systems_block_diags.png
   :align: center
   :width: 600px
   
   IIO-Based Development Systems

Evaluation Boards and Development Platforms
===========================================

Pmod (Peripheral Module)
------------------------

This is a de-facto standard developed by Digilent. Pmods communicate with host boards using 6, 8, or 12-pin, 100-mil pitch connectors that can carry multiple digital control signals, taking advantage of standard serial protocols such as SPI and I²C. The official specification is available from Digilent at https://digilent.com/reference/pmod/start. Pmod evaluation boards on this page are supported on either a ZedBoard or Cora Z7 FPGA carrier board. Pre-built example projects are provided that implement an IIO server, compatible with ACE, Scopy, and any language supported by the libiio (C, C#, Python, MATLAB, etc.)

The Pmod board hardware documentation is at https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/pulsar-adc-pmods 

FMC (FPGA Mezzanine Card)
-------------------------

This is an industry standard, also known as VITA57. FMC is a widely used standard for both COTS and development carriers and module cards. FMC evaluation boards on this page are supported on the ZedBoard carrier board as well as the ADI proprietary SDP-H1 board. Pre-built example projects for the ZedBoard are provided that implement an IIO server, compatible with ACE, Scopy, and any language supported by the libiio (C, C#, Python, MATLAB, etc.) Important: The SDP-H1 is ADI proprietary, and works in conjunction with ACE software or product-specific evaluation software package. It is not intended as a development platform, and source code is not provided.

SDP 120-way interface
---------------------

This is an ADI proprietary standard based on the  Hirose FX8 series connector. These boards interface with the SDP-B or SDP-H1, and work with ACE or product-specific evaluation software package. It is not intended as a development platform, and source code is not provided.


Software Resources
==================

Standard Application Software
-----------------------------
The HDL, Linux, and no-OS example projects are typically based on the Linux Industrial Input-Output (IIO) framework. This maximizes flexibility, as the framework is cross-platform (Windows, Linux, Mac) and supports multiple languages (C, C++, C#, Python, MATLAB, and others). The projects are also supported by the ACE evaluation GUI, and the Scopy multi-purpose data acquisition GUI. 

HDL IP Core
-----------

The HDL for these devices is based on the SPI Engine IP core, user guide here: `SPI Engine <https://analogdevicesinc.github.io/hdl/library/spi_engine/index.html>`_, and PWM IP core, which generates the sample rate from the master clock.

The example project for these devices is described at `PULSAR-ADC HDL project <https://analogdevicesinc.github.io/hdl/projects/pulsar_adc/index.html>`_. 

The example project is parameterized for each device, and building the project generates a set of boot files that can be run on the target platform.

Linux Device Drivers
--------------------

The Linux driver for these devices is presently in development, with the goal of having a single, unified driver covering all devices and the associated HDL code.

The AD400x driver is in upstream review, documented at https://wiki.analog.com/resources/tools-software/linux-drivers/iio-adc/ad400x

The previous mainlined PulSAR family driver is documented at https://wiki.analog.com/resources/tools-software/linux-drivers/iio-adc/ad7476a

The updated device driver is compatible with the HDL example project, and provides a convenient programming interface for controlling the ADC and capturing data.



no-OS (Bare Metal) Device Drivers and Examples
----------------------------------------------

The no-OS driver is intended for systems not using an operating system. It is generally easier to start with a Linux-based system for initial development, then migrate to no-OS.

https://github.com/analogdevicesinc/no-OS/tree/main/projects/pulsar-adc

https://github.com/analogdevicesinc/no-OS/tree/main/drivers/adc/pulsar_adc



Product-Specific Software
-------------------------

The ADI proprietary controller boards typically work with product specific software, either a standalone GUI program, or through ACE via a control board plugin. These allow measurement of typical ADC performance metrics such as SNR, THD, linearity, etc., and saving data out to files.

Board and Platform Summary
==========================

The various eval boards and their supported platforms are listed below. The standard platforms can be used for product performance evaluation using ACE software, software development, and system prototyping. The ADI proprietary platforms are more constrained, and only work with the software listed.

.. Note::

   Only a few example cells are filled out for now.

.. csv-table:: Single-Channel SAR table test
   :file: single_channel_SARs.csv
   :header-rows: 1