EVAL-ADTF3175D-NXZ User Guide
=============================
.. attention::

   This is a draft document in an unofficial fork of `<https://github.com/analogdevicesinc/documentation>`__


News
~~~~

.. important::

   Support or Query: tof@analog.com
   
   **2024-07-29**: Release 5.0.0 is available on GitHub; see
   `ToF/releases <https://github.com/analogdevicesinc/ToF/releases>`__
   
.. important::

   With 5.0.0 the depth compute libraries have been moved
   to the eval kit hardware you may:
   
   -  Some host PCs require an externally power self-powered hub due to the
      increased current usage.
   -  Some host PCs may experience a degradation in frame rate due to
      available USB bandwidth.
   
   

.. important::

   From the ADTF3175D Eval Kit version 4.3.0 ADTF3175
   (Crosby) modules supporting the old modes, QMP and MP, are no longer
   supported. Please check this page for module upgrade information :
   :dokuwiki:`Link </resources/eval/user-guides/eval-adtf3175d-nxz-upgrade-module>`.

User Guide
~~~~~~~~~~

Analog Devices 3D time of flight (ToF) camera products capture depth
information, enabling advanced machine vision applications and allowing
people and devices to sense, capture and interact with their spatial
environments.

For more information see: `Time of Flight Camera – System Overview <https://www.analog.com/en/analog-dialogue/articles/time-of-flight-system-design-part-1-system-overview.html>`__

Introduction
------------

The EVAL-ADTF3175D-NXZ time of flight (ToF) evaluation kit is showcasing
the ADTF3175 module with ADI's depth ISP, the ADSD3500. The kit supports
ethernet over USB connectivity to a PC for real-time visualization,
capture and post processing of depth data. The kit includes host PC
software (Windows) and an open source multi-platform SDK for custom
application development.

Key Features
~~~~~~~~~~~~

.. list-table::

   - 

      - Resolution:
      - 
      - 1024x1024 TOF sensor
   - 

      - Illumination:
      - 
      - FOI 81°x81° - 940nm Lumentum VCSEL
   - 

      - Field of view:
      - 
      - FOV 75°x75°
   - 

      - Operating range:
      - 
      - 0.4 to 4m @ 15% reflectance (native)
   - 

      - Depth Noise:
      - 
      - <15mm
   - 

      - Accuracy:
      - 
      - +/- 3mm depth error

Modes of Operation
~~~~~~~~~~~~~~~~~~

See the :dokuwiki:`Modes Table </resources/eval/user-guides/eval-adtf3175d-nxz/mode_table>`
page.

What is included in the kit?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  ADTF3175D Evaluation Module

   -  ADTF3175 Module
   -  i.MX8 M Plus SOM (SolidRun)
   -  Camera Interface Board
   -  ADSD3500 Interposer board

-  16GB flashed microSD card (Inserted in module sd card slot)
-  USB-C to USB-C cable. Supports PD 2.0, and USB 3.1
-  Tripod

|crosby2.jpg|

--------------

System Overview
---------------

Quarter-MegaPixel (512x512)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image1|

MegaPixel (1024x1024)
~~~~~~~~~~~~~~~~~~~~~

|image2|

:dokuwiki:`Click here for more information on each block </resources/eval/user-guides/eval-adtf3175-nxz/adtf3175d-bc>`

Quick Start
-----------

:dokuwiki:`Start Up Guide </eval-adtf3175d-nxz-startup>`

--------------

System Information
------------------

::

   ; USB and Power : 

**Minimum Requirements**

-  USB 3.0 (5Gbps)
-  USB Type-C cable
-  2.0A

**Recommended Requirements**

-  USB 3.1 Gen2
-  USB Type-C cable
-  3.0A

Note: Do not use USB Type-C to USB Type-A adapters.

::

   ; Dimensions : 66mm x 58.6mm x 67.9mm
   ; Enclosure Drawing : {{ :resources:eval:user-guides:eval-adtf3175d-nxz_drawing_v1.pdf | Link}}
   ; Laser Safety : Class 1
   ; Operating Environment : //TO BE COMPLETED//

--------------

Index of Pages
--------------

.. Note::

   These are absolute links to existing wiki pages for the time being.

-  :dokuwiki:`Start Up Guide <https://wiki.analog.com/eval-adtf3175d-nxz-startup>`
-  :dokuwiki:`Workflow <https://wiki.analog.com/resources/eval/user-guides/eval-adtf3175d-nxz/workflow>`
-  System Maintenance

      * `Installation <https://wiki.analog.com/resources/eval/user-guides/eval-adsd3100-nxz-software-installation>`__
      * `System Update <https://wiki.analog.com/resources/eval/user-guides/eval-adtf3175d-nxz/system_update>`__
      * `Accessing the ADTF3175D <https://wiki.analog.com/resources/eval/user-guides/eval-adtf3175x-access>`__
      * `Troubleshooting Guide <https://wiki.analog.com/resources/eval/user-guides/aditofgui_ts>`__
   * Tools
      * `ADIToFGUI Tool <https://wiki.analog.com/resources/eval/user-guides/eval-adsd3100-nxz-gui>`__
      * `Data Collect CLI Tool <https://wiki.analog.com/resources/eval/user-guides/eval-adsd3100-nxz-gui/datacollect_cli>`__
      * `Python Tools <https://wiki.analog.com/resources/eval/user-guides/eval-adsd3100-nxz/tof_auxtools_cli>`__
      * `Depth Compute CLI Tool (4.3.0 or older) <https://wiki.analog.com/resources/eval/user-guides/eval-adsd3100-nxz/depthcompute_cli>`__
   * `SDK Development <https://wiki.analog.com/resources/eval/user-guides/eval-adsd3100-nxz-development>`__
   * `V4L2 Device Driver <https://wiki.analog.com/resources/eval/user-guides/eval-adsd3175d-v4l2-device-driver>`__
   * `ADSD3500 Guide <https://wiki.analog.com/resources/eval/user-guides/eval-adtf3175x-adsd3500>`__

--------------

Support Links
-------------

-  Module and Eval kit questions :
   `EngineerZone <ez>depth-perception-ranging-technologies/continuous-wave-cmos-time-of-flight-tof/>`__
-  Software/SDK questions : `ToF/issues <repo>ToF/issues>`__
-  Lumentum VSCEL Information :

   #. https://www.lumentum.com/en/products/10-w-940-nm-triple-junction-vcsel-array
   #. https://www.lumentum.com/en/products/multi-junction-vcsel-arrays

Terms
-----


   - **FOI** : Field of Illumination
   - **FOV** : Field of View
   - **FPS** : Frames per Second
   - **SOM** : System On Module
   - **VCSEL** : Vertical-Cavity Surface-Emitting Laser

.. |crosby2.jpg| image:: crosby2.jpg
   :width: 300px
.. |image1| image:: pulsatrix_qmp.png
.. |image2| image:: pulsatrix_mp.png
