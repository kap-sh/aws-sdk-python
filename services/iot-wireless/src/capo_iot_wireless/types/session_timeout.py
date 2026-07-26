"""Generated from Smithy shape ``com.amazonaws.iotwireless#SessionTimeout``."""

from typing import TypeAlias

"""<p>How long before a multicast group session is to timeout.</p> <note> <p>We recommend that you provide a timeout value that is a power-of-two (such as 64, 128, 256). If a non-power-of-two value is provided, it will automatically be rounded up to the next supported power-of-two within the allowed range.</p> </note>"""
SessionTimeout: TypeAlias = int
