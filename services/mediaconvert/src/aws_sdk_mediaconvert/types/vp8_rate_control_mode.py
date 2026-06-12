"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Vp8RateControlMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""With the VP8 codec, you can use only the variable bitrate (VBR) rate control mode."""
Vp8RateControlMode: TypeAlias = Literal["VBR",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("VBR",))


def serialize_json(value: Vp8RateControlMode) -> str:
    return value


def deserialize_json(data: str) -> Vp8RateControlMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Vp8RateControlMode value: {data!r}")
    return cast(Vp8RateControlMode, data)
