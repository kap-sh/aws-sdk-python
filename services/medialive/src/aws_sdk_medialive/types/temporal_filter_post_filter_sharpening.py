"""Generated from Smithy shape ``com.amazonaws.medialive#TemporalFilterPostFilterSharpening``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Temporal Filter Post Filter Sharpening"""
TemporalFilterPostFilterSharpening: TypeAlias = Literal[
    "AUTO",
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTO",
        "DISABLED",
        "ENABLED",
    )
)


def serialize_json(value: TemporalFilterPostFilterSharpening) -> str:
    return value


def deserialize_json(data: str) -> TemporalFilterPostFilterSharpening:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown TemporalFilterPostFilterSharpening value: {data!r}"
        )
    return cast(TemporalFilterPostFilterSharpening, data)
