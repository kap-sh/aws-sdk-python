"""Generated from Smithy shape ``com.amazonaws.medialive#DvbSubDestinationShadowColor``."""

from typing import Literal, TypeAlias, cast

"""Dvb Sub Destination Shadow Color"""
DvbSubDestinationShadowColor: TypeAlias = Literal[
    "BLACK",
    "NONE",
    "WHITE",
]


# --- restJson1 ser/de ---
def serialize_json(value: DvbSubDestinationShadowColor) -> str:
    return value


def deserialize_json(data: str) -> DvbSubDestinationShadowColor:
    return cast(DvbSubDestinationShadowColor, data)
