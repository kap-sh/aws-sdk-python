"""Generated from Smithy shape ``com.amazonaws.medialive#AvailBlankingState``."""

from typing import Literal, TypeAlias, cast

"""Avail Blanking State"""
AvailBlankingState: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AvailBlankingState) -> str:
    return value


def deserialize_json(data: str) -> AvailBlankingState:
    return cast(AvailBlankingState, data)
