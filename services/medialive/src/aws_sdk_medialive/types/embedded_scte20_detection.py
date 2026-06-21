"""Generated from Smithy shape ``com.amazonaws.medialive#EmbeddedScte20Detection``."""

from typing import Literal, TypeAlias, cast

"""Embedded Scte20 Detection"""
EmbeddedScte20Detection: TypeAlias = Literal[
    "AUTO",
    "OFF",
]


# --- restJson1 ser/de ---
def serialize_json(value: EmbeddedScte20Detection) -> str:
    return value


def deserialize_json(data: str) -> EmbeddedScte20Detection:
    return cast(EmbeddedScte20Detection, data)
