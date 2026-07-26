"""Generated from Smithy shape ``com.amazonaws.medialive#EmbeddedConvert608To708``."""

from typing import Literal, TypeAlias, cast

"""Embedded Convert608 To708"""
EmbeddedConvert608To708: TypeAlias = Literal[
    "DISABLED",
    "UPCONVERT",
]


# --- restJson1 ser/de ---
def serialize_json(value: EmbeddedConvert608To708) -> str:
    return value


def deserialize_json(data: str) -> EmbeddedConvert608To708:
    return cast(EmbeddedConvert608To708, data)
