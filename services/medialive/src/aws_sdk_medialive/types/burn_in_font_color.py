"""Generated from Smithy shape ``com.amazonaws.medialive#BurnInFontColor``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Burn In Font Color"""
BurnInFontColor: TypeAlias = Literal[
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


def serialize_json(value: BurnInFontColor) -> str:
    return value


def deserialize_json(data: str) -> BurnInFontColor:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BurnInFontColor value: {data!r}")
    return cast(BurnInFontColor, data)
