EVAL-ADXL355-PMDZ
#####################################################

.. NOTE::

   This page is intended to cover only the EVAL-ADXL335-PMDZ board, and is a work in progress. For documentation on all available hardware and software for the ADXL355, refer to its product solution center.


The :adi:`EVAL-ADXL355-PMDZ` is a compact, low-cost, Pmod-compatible evaluation board for the ADXL355. It targets several standard microcontroller development boards that either have a native Pmod interface, or via an adapter. It also targets the Raspberry Pi via the :adi:`PMD-RPI-INTZ` adapter board. The Pmod board is small in size with dimensions approximately 2.5 cm in width by 2.5 cm in length.

SPI PMOD peripheral connectors can also be found on many 3rd party MCU or FPGA development boards, where the EVAL-ADXL355-PMDZ can be connected directly into those systems, and you can develop your own code using our reference code below.

.. image:: EVAL-ADXL335-PMDZANGLE-web.png
   :width: 350px

Developing with the ADXL355
===========================

The EVAL-ADXL335-PMDZ will be used for the various example systems described below. These examples are designed to be used as-is for initial development, then ported to your target hardware.

.. image:: adxl355_pmdz.png
   :width: 350px

Pmod  Processor Connector
-------------------------

The PMOD interface is a series of standardized digital interfaces for various
digital communication protocols such as SPI, I2C, and UART. These interface
types were standardized by Digilent, which is now a division of National
Instruments. Complete details on the Pmod specification can be found on the
`Digilent Pmod landing page <https://digilent.com/reference/pmod/start>`__.

The specific interface used for the EVAL-ADXL355-PMDZ boards is the extended
SPI. In general ADI has adopted the extended SPI connector for all PMOD devices
which have an SPI interface. It provides flexibility to add interrupts, general
purpose I/O, resets, and other digitally controlled functions.

+---------------+---------------------+----------+---------------+----------------+----------+
| P1 Pin Number | Pin Function        | Mnemonic | P1 Pin Number | Pin Function   | Mnemonic |
+===============+=====================+==========+===============+================+==========+
| Pin 1         | Chip Select         | CS       | Pin 7         | Interrupt 1    | INT1     |
+---------------+---------------------+----------+---------------+----------------+----------+
| Pin 2         | Master Out Slave In | MOSI     | Pin 8         | Not Connected  | NC       |
+---------------+---------------------+----------+---------------+----------------+----------+
| Pin 3         | Master In Slave Out | MISO     | Pin 9         | Interrupt 2    | INT2     |
+---------------+---------------------+----------+---------------+----------------+----------+
| Pin 4         | Serial Clock        | SCLK     | Pin 10        | Data Ready     | DRDY     |
+---------------+---------------------+----------+---------------+----------------+----------+
| Pin 5         | Digital Ground      | DGND     | Pin 11        | Digital Ground | DGND     |
+---------------+---------------------+----------+---------------+----------------+----------+
| Pin 6         | Digital Power       | VDD      | Pin 12        | Digital Power  | VDD      |
+---------------+---------------------+----------+---------------+----------------+----------+

.. image:: adxl355_layout.png
   :width: 300px

ADXL355 Interrupt Pins
----------------------

The EVAL-ADXL355-PMDZ has two interrupt pins and a data ready pin which can be
used as external indicators for the user. The interrupt pins can be programmed
through software to reflect various status flags within the ADXL355, and those
pins are accessible through the SPI PMOD header. For complete details on the
individual status flags, what they mean, and how to program the chip to reflect
those interrupts, please consult the :adi:`ADXL355` data sheet.

Power Supply Considerations and Configuration
---------------------------------------------

When using the ADXL355 PMOD board, the 3.3V power for the PMOD comes directly
from the host board it is connected to. Most Pmod platform boards can supply at
least 100 mA, more than adquate for the EVAL-ADXL355-PMDZ.