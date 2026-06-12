"""Generated from Smithy shape ``com.amazonaws.medialive#Eac3PassthroughControl``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Eac3 Passthrough Control"""
Eac3PassthroughControl: TypeAlias = Literal[
    "NO_PASSTHROUGH",
    "WHEN_POSSIBLE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NO_PASSTHROUGH",
        "WHEN_POSSIBLE",
    )
)


def serialize_json(value: Eac3PassthroughControl) -> str:
    return value


def deserialize_json(data: str) -> Eac3PassthroughControl:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Eac3PassthroughControl value: {data!r}")
    return cast(Eac3PassthroughControl, data)
