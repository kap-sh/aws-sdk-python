"""Generated from Smithy shape ``com.amazonaws.medialive#BlackoutSlateState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Blackout Slate State"""
BlackoutSlateState: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "ENABLED",
    )
)


def serialize_json(value: BlackoutSlateState) -> str:
    return value


def deserialize_json(data: str) -> BlackoutSlateState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BlackoutSlateState value: {data!r}")
    return cast(BlackoutSlateState, data)
