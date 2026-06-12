"""Generated from Smithy shape ``com.amazonaws.medialive#Av1TemporalAq``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Av1 Temporal Aq"""
Av1TemporalAq: TypeAlias = Literal[
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


def serialize_json(value: Av1TemporalAq) -> str:
    return value


def deserialize_json(data: str) -> Av1TemporalAq:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Av1TemporalAq value: {data!r}")
    return cast(Av1TemporalAq, data)
