"""Generated from Smithy shape ``com.amazonaws.medialive#Scte35InputMode``."""

from typing import Literal, TypeAlias, cast

"""Whether the SCTE-35 input should be the active input or a fixed input."""
Scte35InputMode: TypeAlias = Literal[
    "FIXED",
    "FOLLOW_ACTIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: Scte35InputMode) -> str:
    return value


def deserialize_json(data: str) -> Scte35InputMode:
    return cast(Scte35InputMode, data)
