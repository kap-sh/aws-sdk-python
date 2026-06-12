"""Generated from Smithy shape ``com.amazonaws.medialive#DvbSubDestinationShadowColor``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Dvb Sub Destination Shadow Color"""
DvbSubDestinationShadowColor: TypeAlias = Literal[
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


def serialize_json(value: DvbSubDestinationShadowColor) -> str:
    return value


def deserialize_json(data: str) -> DvbSubDestinationShadowColor:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DvbSubDestinationShadowColor value: {data!r}"
        )
    return cast(DvbSubDestinationShadowColor, data)
