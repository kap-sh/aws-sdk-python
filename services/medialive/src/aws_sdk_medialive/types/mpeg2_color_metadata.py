"""Generated from Smithy shape ``com.amazonaws.medialive#Mpeg2ColorMetadata``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Mpeg2 Color Metadata"""
Mpeg2ColorMetadata: TypeAlias = Literal[
    "IGNORE",
    "INSERT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IGNORE",
        "INSERT",
    )
)


def serialize_json(value: Mpeg2ColorMetadata) -> str:
    return value


def deserialize_json(data: str) -> Mpeg2ColorMetadata:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Mpeg2ColorMetadata value: {data!r}")
    return cast(Mpeg2ColorMetadata, data)
