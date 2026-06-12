"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Vp9RateControlMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""With the VP9 codec, you can use only the variable bitrate (VBR) rate control mode."""
Vp9RateControlMode: TypeAlias = Literal["VBR",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("VBR",))


def serialize_json(value: Vp9RateControlMode) -> str:
    return value


def deserialize_json(data: str) -> Vp9RateControlMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Vp9RateControlMode value: {data!r}")
    return cast(Vp9RateControlMode, data)
