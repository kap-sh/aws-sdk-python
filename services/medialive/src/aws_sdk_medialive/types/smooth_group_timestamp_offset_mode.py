"""Generated from Smithy shape ``com.amazonaws.medialive#SmoothGroupTimestampOffsetMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Smooth Group Timestamp Offset Mode"""
SmoothGroupTimestampOffsetMode: TypeAlias = Literal[
    "USE_CONFIGURED_OFFSET",
    "USE_EVENT_START_DATE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USE_CONFIGURED_OFFSET",
        "USE_EVENT_START_DATE",
    )
)


def serialize_json(value: SmoothGroupTimestampOffsetMode) -> str:
    return value


def deserialize_json(data: str) -> SmoothGroupTimestampOffsetMode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SmoothGroupTimestampOffsetMode value: {data!r}"
        )
    return cast(SmoothGroupTimestampOffsetMode, data)
