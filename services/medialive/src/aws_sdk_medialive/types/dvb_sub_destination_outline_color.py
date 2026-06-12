"""Generated from Smithy shape ``com.amazonaws.medialive#DvbSubDestinationOutlineColor``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Dvb Sub Destination Outline Color"""
DvbSubDestinationOutlineColor: TypeAlias = Literal[
    "BLACK",
    "BLUE",
    "GREEN",
    "RED",
    "WHITE",
    "YELLOW",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BLACK",
        "BLUE",
        "GREEN",
        "RED",
        "WHITE",
        "YELLOW",
    )
)


def serialize_json(value: DvbSubDestinationOutlineColor) -> str:
    return value


def deserialize_json(data: str) -> DvbSubDestinationOutlineColor:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DvbSubDestinationOutlineColor value: {data!r}"
        )
    return cast(DvbSubDestinationOutlineColor, data)
