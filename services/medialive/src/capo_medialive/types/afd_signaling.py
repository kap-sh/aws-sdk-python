"""Generated from Smithy shape ``com.amazonaws.medialive#AfdSignaling``."""

from typing import Literal, TypeAlias, cast

"""Afd Signaling"""
AfdSignaling: TypeAlias = Literal[
    "AUTO",
    "FIXED",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: AfdSignaling) -> str:
    return value


def deserialize_json(data: str) -> AfdSignaling:
    return cast(AfdSignaling, data)
