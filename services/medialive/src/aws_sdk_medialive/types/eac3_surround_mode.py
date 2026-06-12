"""Generated from Smithy shape ``com.amazonaws.medialive#Eac3SurroundMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Eac3 Surround Mode"""
Eac3SurroundMode: TypeAlias = Literal[
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


def serialize_json(value: Eac3SurroundMode) -> str:
    return value


def deserialize_json(data: str) -> Eac3SurroundMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Eac3SurroundMode value: {data!r}")
    return cast(Eac3SurroundMode, data)
