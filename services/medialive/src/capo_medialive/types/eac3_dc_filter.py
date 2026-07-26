"""Generated from Smithy shape ``com.amazonaws.medialive#Eac3DcFilter``."""

from typing import Literal, TypeAlias, cast

"""Eac3 Dc Filter"""
Eac3DcFilter: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: Eac3DcFilter) -> str:
    return value


def deserialize_json(data: str) -> Eac3DcFilter:
    return cast(Eac3DcFilter, data)
