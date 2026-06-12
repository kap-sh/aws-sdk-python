"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Eac3AtmosSurroundExMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify whether your input audio has an additional center rear surround channel matrix encoded into your left and right surround channels."""
Eac3AtmosSurroundExMode: TypeAlias = Literal[
    "NOT_INDICATED",
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NOT_INDICATED",
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: Eac3AtmosSurroundExMode) -> str:
    return value


def deserialize_json(data: str) -> Eac3AtmosSurroundExMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Eac3AtmosSurroundExMode value: {data!r}")
    return cast(Eac3AtmosSurroundExMode, data)
