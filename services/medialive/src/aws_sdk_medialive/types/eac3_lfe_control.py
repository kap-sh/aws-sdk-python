"""Generated from Smithy shape ``com.amazonaws.medialive#Eac3LfeControl``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Eac3 Lfe Control"""
Eac3LfeControl: TypeAlias = Literal[
    "LFE",
    "NO_LFE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LFE",
        "NO_LFE",
    )
)


def serialize_json(value: Eac3LfeControl) -> str:
    return value


def deserialize_json(data: str) -> Eac3LfeControl:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Eac3LfeControl value: {data!r}")
    return cast(Eac3LfeControl, data)
