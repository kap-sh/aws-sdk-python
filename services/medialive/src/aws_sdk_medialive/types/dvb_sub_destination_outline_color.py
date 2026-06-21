"""Generated from Smithy shape ``com.amazonaws.medialive#DvbSubDestinationOutlineColor``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: DvbSubDestinationOutlineColor) -> str:
    return value


def deserialize_json(data: str) -> DvbSubDestinationOutlineColor:
    return cast(DvbSubDestinationOutlineColor, data)
