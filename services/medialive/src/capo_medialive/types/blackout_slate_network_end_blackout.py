"""Generated from Smithy shape ``com.amazonaws.medialive#BlackoutSlateNetworkEndBlackout``."""

from typing import Literal, TypeAlias, cast

"""Blackout Slate Network End Blackout"""
BlackoutSlateNetworkEndBlackout: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: BlackoutSlateNetworkEndBlackout) -> str:
    return value


def deserialize_json(data: str) -> BlackoutSlateNetworkEndBlackout:
    return cast(BlackoutSlateNetworkEndBlackout, data)
