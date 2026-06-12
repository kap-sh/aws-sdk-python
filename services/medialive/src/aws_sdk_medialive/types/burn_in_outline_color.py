"""Generated from Smithy shape ``com.amazonaws.medialive#BurnInOutlineColor``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Burn In Outline Color"""
BurnInOutlineColor: TypeAlias = Literal[
    "BLACK",
    "BLUE",
    "GREEN",
    "RED",
    "WHITE",
    "YELLOW",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BLACK",
        "BLUE",
        "GREEN",
        "RED",
        "WHITE",
        "YELLOW",
    )
)


def serialize_json(value: BurnInOutlineColor) -> str:
    return value


def deserialize_json(data: str) -> BurnInOutlineColor:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BurnInOutlineColor value: {data!r}")
    return cast(BurnInOutlineColor, data)
