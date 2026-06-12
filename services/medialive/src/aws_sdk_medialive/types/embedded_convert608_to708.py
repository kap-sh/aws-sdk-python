"""Generated from Smithy shape ``com.amazonaws.medialive#EmbeddedConvert608To708``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Embedded Convert608 To708"""
EmbeddedConvert608To708: TypeAlias = Literal[
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


def serialize_json(value: EmbeddedConvert608To708) -> str:
    return value


def deserialize_json(data: str) -> EmbeddedConvert608To708:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EmbeddedConvert608To708 value: {data!r}")
    return cast(EmbeddedConvert608To708, data)
