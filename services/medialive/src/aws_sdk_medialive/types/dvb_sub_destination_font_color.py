"""Generated from Smithy shape ``com.amazonaws.medialive#DvbSubDestinationFontColor``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: DvbSubDestinationFontColor) -> str:
    return value


def deserialize_json(data: str) -> DvbSubDestinationFontColor:
    return cast(DvbSubDestinationFontColor, data)
