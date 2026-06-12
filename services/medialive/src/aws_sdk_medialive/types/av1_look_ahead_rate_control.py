"""Generated from Smithy shape ``com.amazonaws.medialive#Av1LookAheadRateControl``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Av1 Look Ahead Rate Control"""
Av1LookAheadRateControl: TypeAlias = Literal[
    "HIGH",
    "LOW",
    "MEDIUM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HIGH",
        "LOW",
        "MEDIUM",
    )
)


def serialize_json(value: Av1LookAheadRateControl) -> str:
    return value


def deserialize_json(data: str) -> Av1LookAheadRateControl:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Av1LookAheadRateControl value: {data!r}")
    return cast(Av1LookAheadRateControl, data)
