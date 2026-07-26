"""Generated from Smithy shape ``com.amazonaws.medialive#Ac3LfeFilter``."""

from typing import Literal, TypeAlias, cast

"""Ac3 Lfe Filter"""
Ac3LfeFilter: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: Ac3LfeFilter) -> str:
    return value


def deserialize_json(data: str) -> Ac3LfeFilter:
    return cast(Ac3LfeFilter, data)
