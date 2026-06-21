"""Generated from Smithy shape ``com.amazonaws.medialive#DvbSubDestinationTeletextGridControl``."""

from typing import Literal, TypeAlias, cast

"""Dvb Sub Destination Teletext Grid Control"""
DvbSubDestinationTeletextGridControl: TypeAlias = Literal[
    "FIXED",
    "SCALED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DvbSubDestinationTeletextGridControl) -> str:
    return value


def deserialize_json(data: str) -> DvbSubDestinationTeletextGridControl:
    return cast(DvbSubDestinationTeletextGridControl, data)
