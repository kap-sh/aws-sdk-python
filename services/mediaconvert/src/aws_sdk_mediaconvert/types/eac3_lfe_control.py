"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Eac3LfeControl``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""When encoding 3/2 audio, controls whether the LFE channel is enabled"""
Eac3LfeControl: TypeAlias = Literal[
    "LFE",
    "NO_LFE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LFE",
        "NO_LFE",
    )
)


def serialize_json(value: Eac3LfeControl) -> str:
    return value


def deserialize_json(data: str) -> Eac3LfeControl:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Eac3LfeControl value: {data!r}")
    return cast(Eac3LfeControl, data)
