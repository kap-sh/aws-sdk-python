"""Generated from Smithy shape ``com.amazonaws.medialive#Mpeg2ColorSpace``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Mpeg2 Color Space"""
Mpeg2ColorSpace: TypeAlias = Literal[
    "AUTO",
    "PASSTHROUGH",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTO",
        "PASSTHROUGH",
    )
)


def serialize_json(value: Mpeg2ColorSpace) -> str:
    return value


def deserialize_json(data: str) -> Mpeg2ColorSpace:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Mpeg2ColorSpace value: {data!r}")
    return cast(Mpeg2ColorSpace, data)
