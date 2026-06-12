"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Ac3LfeFilter``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Applies a 120Hz lowpass filter to the LFE channel prior to encoding. Only valid with 3_2_LFE coding mode."""
Ac3LfeFilter: TypeAlias = Literal[
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


def serialize_json(value: Ac3LfeFilter) -> str:
    return value


def deserialize_json(data: str) -> Ac3LfeFilter:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Ac3LfeFilter value: {data!r}")
    return cast(Ac3LfeFilter, data)
