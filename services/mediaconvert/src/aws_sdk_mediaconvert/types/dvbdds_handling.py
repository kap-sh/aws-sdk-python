"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DvbddsHandling``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify how MediaConvert handles the display definition segment (DDS). To exclude the DDS from this set of captions: Keep the default, None. To include the DDS: Choose Specified. When you do, also specify the offset coordinates of the display window with DDS x-coordinate and DDS y-coordinate. To include the DDS, but not include display window data: Choose No display window. When you do, you can write position metadata to the page composition segment (PCS) with DDS x-coordinate and DDS y-coordinate. For video resolutions with a height of 576 pixels or less, MediaConvert doesn't include the DDS, regardless of the value you choose for DDS handling. All burn-in and DVB-Sub font settings must match. To include the DDS, with optimized subtitle placement and reduced data overhead: We recommend that you choose Specified (optimal). This option provides the same visual positioning as Specified while using less bandwidth. This also supports resolutions higher than 1080p while maintaining full DVB-Sub compatibility. When you do, also specify the offset coordinates of the display window with DDS x-coordinate and DDS y-coordinate."""
DvbddsHandling: TypeAlias = Literal[
    "NONE",
    "SPECIFIED",
    "NO_DISPLAY_WINDOW",
    "SPECIFIED_OPTIMAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "SPECIFIED",
        "NO_DISPLAY_WINDOW",
        "SPECIFIED_OPTIMAL",
    )
)


def serialize_json(value: DvbddsHandling) -> str:
    return value


def deserialize_json(data: str) -> DvbddsHandling:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DvbddsHandling value: {data!r}")
    return cast(DvbddsHandling, data)
