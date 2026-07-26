"""Generated from Smithy shape ``com.amazonaws.medialive#DvbSubDestinationBackgroundColor``."""

from typing import Literal, TypeAlias, cast

"""Dvb Sub Destination Background Color"""
DvbSubDestinationBackgroundColor: TypeAlias = Literal[
    "BLACK",
    "NONE",
    "WHITE",
]


# --- restJson1 ser/de ---
def serialize_json(value: DvbSubDestinationBackgroundColor) -> str:
    return value


def deserialize_json(data: str) -> DvbSubDestinationBackgroundColor:
    return cast(DvbSubDestinationBackgroundColor, data)
