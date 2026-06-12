"""Generated from Smithy shape ``com.amazonaws.medialive#Eac3PhaseControl``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Eac3 Phase Control"""
Eac3PhaseControl: TypeAlias = Literal[
    "NO_SHIFT",
    "SHIFT_90_DEGREES",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NO_SHIFT",
        "SHIFT_90_DEGREES",
    )
)


def serialize_json(value: Eac3PhaseControl) -> str:
    return value


def deserialize_json(data: str) -> Eac3PhaseControl:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Eac3PhaseControl value: {data!r}")
    return cast(Eac3PhaseControl, data)
