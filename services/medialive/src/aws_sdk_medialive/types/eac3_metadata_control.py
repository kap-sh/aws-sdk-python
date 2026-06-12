"""Generated from Smithy shape ``com.amazonaws.medialive#Eac3MetadataControl``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Eac3 Metadata Control"""
Eac3MetadataControl: TypeAlias = Literal[
    "FOLLOW_INPUT",
    "USE_CONFIGURED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FOLLOW_INPUT",
        "USE_CONFIGURED",
    )
)


def serialize_json(value: Eac3MetadataControl) -> str:
    return value


def deserialize_json(data: str) -> Eac3MetadataControl:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Eac3MetadataControl value: {data!r}")
    return cast(Eac3MetadataControl, data)
