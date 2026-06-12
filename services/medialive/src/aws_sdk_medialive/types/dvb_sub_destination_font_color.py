"""Generated from Smithy shape ``com.amazonaws.medialive#DvbSubDestinationFontColor``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Dvb Sub Destination Font Color"""
DvbSubDestinationFontColor: TypeAlias = Literal[
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


def serialize_json(value: DvbSubDestinationFontColor) -> str:
    return value


def deserialize_json(data: str) -> DvbSubDestinationFontColor:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DvbSubDestinationFontColor value: {data!r}"
        )
    return cast(DvbSubDestinationFontColor, data)
