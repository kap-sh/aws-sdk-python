"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Eac3LfeFilter``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Applies a 120Hz lowpass filter to the LFE channel prior to encoding. Only valid with 3_2_LFE coding mode."""
Eac3LfeFilter: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: Eac3LfeFilter) -> str:
    return value


def deserialize_json(data: str) -> Eac3LfeFilter:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Eac3LfeFilter value: {data!r}")
    return cast(Eac3LfeFilter, data)
