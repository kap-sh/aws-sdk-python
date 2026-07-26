"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Mp4MoovPlacement``."""

from typing import Literal, TypeAlias, cast

"""To place the MOOV atom at the beginning of your output, which is useful for progressive downloading: Leave blank or choose Progressive download. To place the MOOV at the end of your output: Choose Normal."""
Mp4MoovPlacement: TypeAlias = Literal[
    "PROGRESSIVE_DOWNLOAD",
    "NORMAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: Mp4MoovPlacement) -> str:
    return value


def deserialize_json(data: str) -> Mp4MoovPlacement:
    return cast(Mp4MoovPlacement, data)
