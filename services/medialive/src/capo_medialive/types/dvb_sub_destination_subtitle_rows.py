"""Generated from Smithy shape ``com.amazonaws.medialive#DvbSubDestinationSubtitleRows``."""

from typing import Literal, TypeAlias, cast

"""Dvb Sub Destination Subtitle Rows"""
DvbSubDestinationSubtitleRows: TypeAlias = Literal[
    "ROWS_16",
    "ROWS_20",
    "ROWS_24",
]


# --- restJson1 ser/de ---
def serialize_json(value: DvbSubDestinationSubtitleRows) -> str:
    return value


def deserialize_json(data: str) -> DvbSubDestinationSubtitleRows:
    return cast(DvbSubDestinationSubtitleRows, data)
