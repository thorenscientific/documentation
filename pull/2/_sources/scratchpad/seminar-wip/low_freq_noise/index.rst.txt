.. low_freq_noise:

Low Frequency Noise KWIK Lecture + Lab
======================================

General Description
-------------------

The Low Frequency Noise Know-how with Integrated Knowledge (KWIK) Lecture and Lab is a training module regarding amplifier noise. It is a combination of a lecture and a hands-on activity to understand the amplifier noise, especially low frequency noise.

The Low Frequency Noise KWIK Demo provides a lecture material about the importance of noise, noise in time/frequency domain, types of noise, thermal noise in resistors, transistors, and amplifier. It also includes calculation and simulations using LTspice and ADI\ :sup:`SM` Precision Studio.

The Low Frequency Noise KWIK Demo provides a hands-on activity allowing the user to measure the low frequency noise of three general operational amplifiers (op amp): (1) low power op amp, (2) low noise, bipolar op amp, and (3) low noise, zero drift op amp, with the use of ADALM2000 Active Learning Module.

The Low Frequency Noise KWIK Demo uses an easy to use demonstration board, specifically, EVAL-KW4502Z, that directly plugs into the ADALM2000.

Objective
---------

The Low Frequency Noise KWIK Lecture and Lab aims to understand and measure the amplifier low frequency noise. Specifically, to estimate the 0.1 Hz to 10 Hz noise of the three different operational amplifiers, namely, LT1782, ADA4077, and ADA4522, using noise calculations and simulations. Also, to measure the 0.1 Hz to 10 Hz noise of the amplifiers using the EVAL-KW4502Z plugged into ADALM2000. Moreover, the acquired noise in the calculations, simulations, and measurements will be compared to the datasheet information.

Lecture Materials
-----------------

.. ADMONITION:: Download

   :download:`Demystifying Noise Kwik Lecture <demystifying_noise_kwik_lecture.pdf>`

.. ADMONITION:: Download

   :download:`Demystifying Noise Kwik Labs Combined.pdf <demystifying_noise_kwik_labs_combined_.pdf>`

KWIK Demo User Guide
--------------------

A comprehensive User Guide can be found at |EVAL-KW4502Z KWIK Demo User Guide|

.. ADMONITION:: Download

   :download:`EVAL-KW4502Z KWIK Demo User Guide <eval-kw4502z_ug_evkit_rev_0.pdf>`


ADALM2000 Active Learning Module and Scopy
------------------------------------------

`ADALM2000 Active Learning Module <https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/adalm2000.html>`__

`Scopy - A Graphical User Interface (GUI) for the ADALM2000. A multi-functional software toolset with strong capabilities for signal analysis </university/tools/m2k/scopy/>`__

Software Setup Instructions for LTSpice (installation and first time use), ADALM2000 (installation and first time use) and Scopy (installation and first time use)
.. ADMONITION:: Download

   :download:`adalm2000_scopy_and_ltspice_setup_instructions_v1.0.docx <adalm2000_scopy_and_ltspice_setup_instructions_v1.0.docx>`


ADALM2000 Configuration Files
-----------------------------

.. ADMONITION:: Download

   :download:`Configuration files for the ADALM2000 <demystifying_noise_adalm2000_config_files.zip>`

LTspice Simulation Circuits
---------------------------

All LTspice Circuits used are available here:

.. ADMONITION:: Download

   :download:`0.1 Hz to 10 Hz Filter, 60dB LTSpice Simulation Files <0.1_hz_to_10_hz_filter_60db.zip>`

.. NOTE::
   Keep all files in the zip folder in the same folder on your local PC.

--------------

KWIK Demo PCB Image
-------------------

**EVAL-KW502Z Top View**

|eval-kw4502z_top.jpg|

**EVAL-KW502Z Bottom View**

|eval-kw4502z_bottom.jpg|

**EVAL-KW502Z Angle View**

|eval-kw4502z_angle.jpg|


EVAL-KW4502Z Gerber Files
-------------------------

.. ADMONITION:: Download

   :download:`EVAL-KW4502Z Gerber Files <eval-kw4502z_gerber_files.zip>`

Additional Reading
------------------

`Precision Technology Learning Module Amplifiers - Advanced <https://ez.analog.com/amplifiers/w/documents/32480/amplifiers---advanced>`__

`Low Noise Amplifier Selection Guide for Optimal Noise Performance <https://www.analog.com/en/resources/app-notes/an-940.html>`__

`Noise Analysis in Precision Analog Designs <https://www.analog.com/en/resources/media-center/videos/5201716142001.html>`__

`Practical Input-Referred Calculations in Precision Systems <https://www.analog.com/en/resources/analog-dialogue/articles/practical-input-referred-calculations-in-precision-systems.html>`__

`Understanding and Eliminating 1/f Noise <https://www.analog.com/en/resources/analog-dialogue/articles/understanding-and-eliminating-1-f-noise.html>`__


.. |EVAL-KW4502Z KWIK Demo User Guide| image:: eval-kw4502z_ug_evkit_rev_0.pdf

.. |Software Setup Instructions for LTSpice (installation and first time use), ADALM2000 (installation and first time use) and Scopy (installation and first time use)| image:: adalm2000_scopy_and_ltspice_setup_instructions_v1.0.docx
.. |demystifying_noise_adalm2000_config_files.zip| image:: demystifying_noise_adalm2000_config_files.zip
.. |0.1 Hz to 10 Hz Filter, 60dB LTSpice Simulation Files| image:: 0.1_hz_to_10_hz_filter_60db.zip
.. |eval-kw4502z_top.jpg| image:: eval-kw4502z_top.jpg
   :width: 400px
.. |eval-kw4502z_bottom.jpg| image:: eval-kw4502z_bottom.jpg
   :width: 400px
.. |eval-kw4502z_angle.jpg| image:: eval-kw4502z_angle.jpg
   :width: 400px
.. |EVAL-KW4502Z Gerber Files| image:: eval-kw4502z_gerber_files.zip