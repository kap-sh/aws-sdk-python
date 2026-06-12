"""Generated from Smithy shape ``com.amazonaws.medialive#BurnInAlignment``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Burn In Alignment"""
BurnInAlignment: TypeAlias = Literal[
    "CENTERED",
    "LEFT",
    "SMART",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CENTERED",
        "LEFT",
        "SMART",
    )
)


def serialize_json(value: BurnInAlignment) -> str:
    return value


def deserialize_json(data: str) -> BurnInAlignment:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BurnInAlignment value: {data!r}")
    return cast(BurnInAlignment, data)
