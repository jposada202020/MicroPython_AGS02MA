⛔️ DEDEPRECATED
===============

This repository is no longer supported, please consider using alternatives.

.. image:: http://unmaintained.tech/badge.svg
  :target: http://unmaintained.tech
  :alt: No Maintenance Intended


Introduction
============


MicroPython Driver for the AGS02MA TVOC sensor


Installing with mip
====================
To install using mpremote

.. code-block:: shell

    mpremote mip install github:jposada202020/MicroPython_AGS02MA

To install directly using a WIFI capable board

.. code-block:: shell

    mip.install("github:jposada202020/MicroPython_AGS02MA")


Installing Library Examples
============================

If you want to install library examples:

.. code-block:: shell

    mpremote mip install github:jposada202020/MicroPython_AGS02MA/examples.json

To install directly using a WIFI capable board

.. code-block:: shell

    mip.install("github:jposada202020/MicroPython_AGS02MA/examples.json")


Installing from PyPI
=====================

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/micropython-ags02ma/>`_.
To install for current user:

.. code-block:: shell

    pip3 install micropython-ags02ma

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install micropython-ags02ma

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .venv
    source .env/bin/activate
    pip3 install micropython-ags02ma


Usage Example
=============

Take a look at the examples directory

Documentation
=============
API documentation for this library can be found on `Read the Docs <https://micropython-ags02ma.readthedocs.io/en/latest/>`_.
