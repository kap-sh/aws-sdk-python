"""Generated from Smithy shape ``com.amazonaws.medialive#BlackoutSlateState``."""

from typing import Literal, TypeAlias, cast

"""Blackout Slate State"""
BlackoutSlateState: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: BlackoutSlateState) -> str:
    return value


def deserialize_json(data: str) -> BlackoutSlateState:
    return cast(BlackoutSlateState, data)
