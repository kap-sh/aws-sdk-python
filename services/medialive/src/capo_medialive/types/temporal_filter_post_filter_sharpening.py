"""Generated from Smithy shape ``com.amazonaws.medialive#TemporalFilterPostFilterSharpening``."""

from typing import Literal, TypeAlias, cast

"""Temporal Filter Post Filter Sharpening"""
TemporalFilterPostFilterSharpening: TypeAlias = Literal[
    "AUTO",
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: TemporalFilterPostFilterSharpening) -> str:
    return value


def deserialize_json(data: str) -> TemporalFilterPostFilterSharpening:
    return cast(TemporalFilterPostFilterSharpening, data)
