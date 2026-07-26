"""Generated from Smithy shape ``com.amazonaws.mediaconvert#UncompressedTelecine``."""

from typing import Literal, TypeAlias, cast

"""When you do frame rate conversion from 23.976 frames per second (fps) to 29.97 fps, and your output scan type is interlaced, you can optionally enable hard telecine to create a smoother picture. When you keep the default value, None, MediaConvert does a standard frame rate conversion to 29.97 without doing anything with the field polarity to create a smoother picture."""
UncompressedTelecine: TypeAlias = Literal[
    "NONE",
    "HARD",
]


# --- restJson1 ser/de ---
def serialize_json(value: UncompressedTelecine) -> str:
    return value


def deserialize_json(data: str) -> UncompressedTelecine:
    return cast(UncompressedTelecine, data)
