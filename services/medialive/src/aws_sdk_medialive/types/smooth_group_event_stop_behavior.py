"""Generated from Smithy shape ``com.amazonaws.medialive#SmoothGroupEventStopBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Smooth Group Event Stop Behavior"""
SmoothGroupEventStopBehavior: TypeAlias = Literal[
    "NONE",
    "SEND_EOS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "SEND_EOS",
    )
)


def serialize_json(value: SmoothGroupEventStopBehavior) -> str:
    return value


def deserialize_json(data: str) -> SmoothGroupEventStopBehavior:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SmoothGroupEventStopBehavior value: {data!r}"
        )
    return cast(SmoothGroupEventStopBehavior, data)
