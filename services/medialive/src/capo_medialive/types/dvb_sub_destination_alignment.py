"""Generated from Smithy shape ``com.amazonaws.medialive#DvbSubDestinationAlignment``."""

from typing import Literal, TypeAlias, cast

"""Dvb Sub Destination Alignment"""
DvbSubDestinationAlignment: TypeAlias = Literal[
    "CENTERED",
    "LEFT",
    "SMART",
]


# --- restJson1 ser/de ---
def serialize_json(value: DvbSubDestinationAlignment) -> str:
    return value


def deserialize_json(data: str) -> DvbSubDestinationAlignment:
    return cast(DvbSubDestinationAlignment, data)
