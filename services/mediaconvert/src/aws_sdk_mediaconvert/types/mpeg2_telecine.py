"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Mpeg2Telecine``."""

from typing import Literal, TypeAlias, cast

"""When you do frame rate conversion from 23.976 frames per second (fps) to 29.97 fps, and your output scan type is interlaced, you can optionally enable hard or soft telecine to create a smoother picture. Hard telecine produces a 29.97i output. Soft telecine produces an output with a 23.976 output that signals to the video player device to do the conversion during play back. When you keep the default value, None, MediaConvert does a standard frame rate conversion to 29.97 without doing anything with the field polarity to create a smoother picture."""
Mpeg2Telecine: TypeAlias = Literal[
    "NONE",
    "SOFT",
    "HARD",
]


# --- restJson1 ser/de ---
def serialize_json(value: Mpeg2Telecine) -> str:
    return value


def deserialize_json(data: str) -> Mpeg2Telecine:
    return cast(Mpeg2Telecine, data)
