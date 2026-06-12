"""Generated from Smithy shape ``com.amazonaws.medialive#BurnInShadowColor``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Burn In Shadow Color"""
BurnInShadowColor: TypeAlias = Literal[
    "BLACK",
    "NONE",
    "WHITE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BLACK",
        "NONE",
        "WHITE",
    )
)


def serialize_json(value: BurnInShadowColor) -> str:
    return value


def deserialize_json(data: str) -> BurnInShadowColor:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BurnInShadowColor value: {data!r}")
    return cast(BurnInShadowColor, data)
