"""Generated from Smithy shape ``com.amazonaws.medialive#BurnInBackgroundColor``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Burn In Background Color"""
BurnInBackgroundColor: TypeAlias = Literal[
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


def serialize_json(value: BurnInBackgroundColor) -> str:
    return value


def deserialize_json(data: str) -> BurnInBackgroundColor:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BurnInBackgroundColor value: {data!r}")
    return cast(BurnInBackgroundColor, data)
