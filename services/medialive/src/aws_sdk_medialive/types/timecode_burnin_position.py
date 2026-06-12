"""Generated from Smithy shape ``com.amazonaws.medialive#TimecodeBurninPosition``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Timecode Burnin Position"""
TimecodeBurninPosition: TypeAlias = Literal[
    "BOTTOM_CENTER",
    "BOTTOM_LEFT",
    "BOTTOM_RIGHT",
    "MIDDLE_CENTER",
    "MIDDLE_LEFT",
    "MIDDLE_RIGHT",
    "TOP_CENTER",
    "TOP_LEFT",
    "TOP_RIGHT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BOTTOM_CENTER",
        "BOTTOM_LEFT",
        "BOTTOM_RIGHT",
        "MIDDLE_CENTER",
        "MIDDLE_LEFT",
        "MIDDLE_RIGHT",
        "TOP_CENTER",
        "TOP_LEFT",
        "TOP_RIGHT",
    )
)


def serialize_json(value: TimecodeBurninPosition) -> str:
    return value


def deserialize_json(data: str) -> TimecodeBurninPosition:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TimecodeBurninPosition value: {data!r}")
    return cast(TimecodeBurninPosition, data)
