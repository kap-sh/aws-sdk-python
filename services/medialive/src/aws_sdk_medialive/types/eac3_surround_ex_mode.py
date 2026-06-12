"""Generated from Smithy shape ``com.amazonaws.medialive#Eac3SurroundExMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Eac3 Surround Ex Mode"""
Eac3SurroundExMode: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
    "NOT_INDICATED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "ENABLED",
        "NOT_INDICATED",
    )
)


def serialize_json(value: Eac3SurroundExMode) -> str:
    return value


def deserialize_json(data: str) -> Eac3SurroundExMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Eac3SurroundExMode value: {data!r}")
    return cast(Eac3SurroundExMode, data)
