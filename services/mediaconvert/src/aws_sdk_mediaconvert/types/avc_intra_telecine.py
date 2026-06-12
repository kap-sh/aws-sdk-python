"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AvcIntraTelecine``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""When you do frame rate conversion from 23.976 frames per second (fps) to 29.97 fps, and your output scan type is interlaced, you can optionally enable hard telecine to create a smoother picture. When you keep the default value, None, MediaConvert does a standard frame rate conversion to 29.97 without doing anything with the field polarity to create a smoother picture."""
AvcIntraTelecine: TypeAlias = Literal[
    "NONE",
    "HARD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "HARD",
    )
)


def serialize_json(value: AvcIntraTelecine) -> str:
    return value


def deserialize_json(data: str) -> AvcIntraTelecine:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AvcIntraTelecine value: {data!r}")
    return cast(AvcIntraTelecine, data)
