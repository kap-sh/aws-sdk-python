"""Generated from Smithy shape ``com.amazonaws.medialive#AfdSignaling``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Afd Signaling"""
AfdSignaling: TypeAlias = Literal[
    "AUTO",
    "FIXED",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTO",
        "FIXED",
        "NONE",
    )
)


def serialize_json(value: AfdSignaling) -> str:
    return value


def deserialize_json(data: str) -> AfdSignaling:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AfdSignaling value: {data!r}")
    return cast(AfdSignaling, data)
