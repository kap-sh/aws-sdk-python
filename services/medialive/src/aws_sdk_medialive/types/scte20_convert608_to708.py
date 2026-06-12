"""Generated from Smithy shape ``com.amazonaws.medialive#Scte20Convert608To708``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Scte20 Convert608 To708"""
Scte20Convert608To708: TypeAlias = Literal[
    "DISABLED",
    "UPCONVERT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "UPCONVERT",
    )
)


def serialize_json(value: Scte20Convert608To708) -> str:
    return value


def deserialize_json(data: str) -> Scte20Convert608To708:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Scte20Convert608To708 value: {data!r}")
    return cast(Scte20Convert608To708, data)
