"""Generated from Smithy shape ``com.amazonaws.medialive#Ac3MetadataControl``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Ac3 Metadata Control"""
Ac3MetadataControl: TypeAlias = Literal[
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


def serialize_json(value: Ac3MetadataControl) -> str:
    return value


def deserialize_json(data: str) -> Ac3MetadataControl:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Ac3MetadataControl value: {data!r}")
    return cast(Ac3MetadataControl, data)
