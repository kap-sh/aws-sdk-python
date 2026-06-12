"""Generated from Smithy shape ``com.amazonaws.medialive#BlackoutSlateNetworkEndBlackout``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Blackout Slate Network End Blackout"""
BlackoutSlateNetworkEndBlackout: TypeAlias = Literal[
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


def serialize_json(value: BlackoutSlateNetworkEndBlackout) -> str:
    return value


def deserialize_json(data: str) -> BlackoutSlateNetworkEndBlackout:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown BlackoutSlateNetworkEndBlackout value: {data!r}"
        )
    return cast(BlackoutSlateNetworkEndBlackout, data)
