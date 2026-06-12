"""Generated from Smithy shape ``com.amazonaws.medialive#DvbSubDestinationBackgroundColor``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Dvb Sub Destination Background Color"""
DvbSubDestinationBackgroundColor: TypeAlias = Literal[
    "BLACK",
    "NONE",
    "WHITE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BLACK",
        "NONE",
        "WHITE",
    )
)


def serialize_json(value: DvbSubDestinationBackgroundColor) -> str:
    return value


def deserialize_json(data: str) -> DvbSubDestinationBackgroundColor:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DvbSubDestinationBackgroundColor value: {data!r}"
        )
    return cast(DvbSubDestinationBackgroundColor, data)
