"""Generated from Smithy shape ``com.amazonaws.mediaconvert#MovPaddingControl``."""

from typing import Literal, TypeAlias, cast

"""Unless you need Omneon compatibility: Keep the default value, None. To make this output compatible with Omneon: Choose Omneon. When you do, MediaConvert increases the length of the 'elst' edit list atom. Note that this might cause file rejections when a recipient of the output file doesn't expect this extra padding."""
MovPaddingControl: TypeAlias = Literal[
    "OMNEON",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: MovPaddingControl) -> str:
    return value


def deserialize_json(data: str) -> MovPaddingControl:
    return cast(MovPaddingControl, data)
