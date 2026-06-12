"""Generated from Smithy shape ``com.amazonaws.medialive#SmoothGroupEventIdMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Smooth Group Event Id Mode"""
SmoothGroupEventIdMode: TypeAlias = Literal[
    "NO_EVENT_ID",
    "USE_CONFIGURED",
    "USE_TIMESTAMP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NO_EVENT_ID",
        "USE_CONFIGURED",
        "USE_TIMESTAMP",
    )
)


def serialize_json(value: SmoothGroupEventIdMode) -> str:
    return value


def deserialize_json(data: str) -> SmoothGroupEventIdMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SmoothGroupEventIdMode value: {data!r}")
    return cast(SmoothGroupEventIdMode, data)
