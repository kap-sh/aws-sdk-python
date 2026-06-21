"""Generated from Smithy shape ``com.amazonaws.medialive#Eac3LfeFilter``."""

from typing import Literal, TypeAlias, cast

"""Eac3 Lfe Filter"""
Eac3LfeFilter: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: Eac3LfeFilter) -> str:
    return value


def deserialize_json(data: str) -> Eac3LfeFilter:
    return cast(Eac3LfeFilter, data)
