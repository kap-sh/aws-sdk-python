"""Generated from Smithy shape ``com.amazonaws.medialive#BurnInDestinationSubtitleRows``."""

from typing import Literal, TypeAlias, cast

"""Burn In Destination Subtitle Rows"""
BurnInDestinationSubtitleRows: TypeAlias = Literal[
    "ROWS_16",
    "ROWS_20",
    "ROWS_24",
]


# --- restJson1 ser/de ---
def serialize_json(value: BurnInDestinationSubtitleRows) -> str:
    return value


def deserialize_json(data: str) -> BurnInDestinationSubtitleRows:
    return cast(BurnInDestinationSubtitleRows, data)
