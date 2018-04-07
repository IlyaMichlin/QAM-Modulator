# QAM modulator
Modulation is an important part of analog communication. Analog communication is needed to transfer information where we cannot send digital signals. That includes air, cables, optic fibers etc.

The purpose of a modulator is to convers one or more bits to a symbol.

There are many modulation techniques but QAM is probably the most popular. QAM is both an analog and a digital modulation scheme chat combines together PSK and ASK modulations. For more reading refer to Wikipedias "Quadrature amplitude modulation" article:
https://en.wikipedia.org/wiki/Quadrature_amplitude_modulation

My goal was to create a generic QAM modulator. I ended creating a modulator that can:
* Receive data in binary and in raw number form
* Modulate using binary and Gray code constellation
* Modulate any QAM where M=2^2k, k=1,2,3...

## Theory
To create QAM modulation we map the data on a constellation. For QAM-16 using Gray coding can be seen here:

![QAM-16](https://upload.wikimedia.org/wikipedia/commons/d/d1/16QAM_Gray_Coded.png)

As you can see, in QAM-16 each symbol represents 4 bits.
Another important aspect of that image is the Gray coding. In Gray coding nearby symbols differ by only 1 bit. This property helps improve BER. For more reading: http://www.dsplog.com/2008/06/05/16qam-bit-error-gray-mapping/

## Includad files
There are two files:
 * QAM-M.ipynb - explains about the modulator implementation
 * QAM.py - modulator module for use in projects