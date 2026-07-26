"""Generated from Smithy shape ``com.amazonaws.iotwireless#FragmentIntervalMS``."""

from typing import TypeAlias

"""<p>The interval for sending fragments in milliseconds, rounded to the nearest second.</p> <note> <p>This interval only determines the timing for when the Cloud sends down the fragments to yor device. There can be a delay for when your device will receive these fragments. This delay depends on the device's class and the communication delay with the cloud.</p> </note>"""
FragmentIntervalMS: TypeAlias = int
