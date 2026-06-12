"""Generated from Smithy shape ``com.amazonaws.medialive#EmbeddedScte20Detection``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Embedded Scte20 Detection"""
EmbeddedScte20Detection: TypeAlias = Literal[
    "AUTO",
    "OFF",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTO",
        "OFF",
    )
)


def serialize_json(value: EmbeddedScte20Detection) -> str:
    return value


def deserialize_json(data: str) -> EmbeddedScte20Detection:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EmbeddedScte20Detection value: {data!r}")
    return cast(EmbeddedScte20Detection, data)
