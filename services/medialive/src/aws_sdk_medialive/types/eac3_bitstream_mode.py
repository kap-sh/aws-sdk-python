"""Generated from Smithy shape ``com.amazonaws.medialive#Eac3BitstreamMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Eac3 Bitstream Mode"""
Eac3BitstreamMode: TypeAlias = Literal[
    "COMMENTARY",
    "COMPLETE_MAIN",
    "EMERGENCY",
    "HEARING_IMPAIRED",
    "VISUALLY_IMPAIRED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMMENTARY",
        "COMPLETE_MAIN",
        "EMERGENCY",
        "HEARING_IMPAIRED",
        "VISUALLY_IMPAIRED",
    )
)


def serialize_json(value: Eac3BitstreamMode) -> str:
    return value


def deserialize_json(data: str) -> Eac3BitstreamMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Eac3BitstreamMode value: {data!r}")
    return cast(Eac3BitstreamMode, data)
