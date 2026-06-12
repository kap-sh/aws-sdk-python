"""Generated from Smithy shape ``com.amazonaws.medialive#BurnInDestinationSubtitleRows``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Burn In Destination Subtitle Rows"""
BurnInDestinationSubtitleRows: TypeAlias = Literal[
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


def serialize_json(value: BurnInDestinationSubtitleRows) -> str:
    return value


def deserialize_json(data: str) -> BurnInDestinationSubtitleRows:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown BurnInDestinationSubtitleRows value: {data!r}"
        )
    return cast(BurnInDestinationSubtitleRows, data)
