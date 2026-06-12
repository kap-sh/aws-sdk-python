"""Generated from Smithy shape ``com.amazonaws.iotwireless#RedundancyPercent``."""

from typing import TypeAlias

"""<p>The percentage of the added fragments that are redundant. For example, if the size of the firmware image file is 100 bytes and the fragment size is 10 bytes, with <code>RedundancyPercent</code> set to 50(%), the final number of encoded fragments is (100 / 10) + (100 / 10 * 50%) = 15.</p>"""
RedundancyPercent: TypeAlias = int
