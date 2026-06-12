"""Generated from Smithy shape ``com.amazonaws.medialive#DvbSubDestinationSubtitleRows``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Dvb Sub Destination Subtitle Rows"""
DvbSubDestinationSubtitleRows: TypeAlias = Literal[
    "ROWS_16",
    "ROWS_20",
    "ROWS_24",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ROWS_16",
        "ROWS_20",
        "ROWS_24",
    )
)


def serialize_json(value: DvbSubDestinationSubtitleRows) -> str:
    return value


def deserialize_json(data: str) -> DvbSubDestinationSubtitleRows:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DvbSubDestinationSubtitleRows value: {data!r}"
        )
    return cast(DvbSubDestinationSubtitleRows, data)
