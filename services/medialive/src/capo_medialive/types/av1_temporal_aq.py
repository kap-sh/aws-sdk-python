"""Generated from Smithy shape ``com.amazonaws.medialive#Av1TemporalAq``."""

from typing import Literal, TypeAlias, cast

"""Av1 Temporal Aq"""
Av1TemporalAq: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: Av1TemporalAq) -> str:
    return value


def deserialize_json(data: str) -> Av1TemporalAq:
    return cast(Av1TemporalAq, data)
