"""Generated from Smithy shape ``com.amazonaws.medialive#M2tsScte35Control``."""

from typing import Literal, TypeAlias, cast

"""M2ts Scte35 Control"""
M2tsScte35Control: TypeAlias = Literal[
    "NONE",
    "PASSTHROUGH",
]


# --- restJson1 ser/de ---
def serialize_json(value: M2tsScte35Control) -> str:
    return value


def deserialize_json(data: str) -> M2tsScte35Control:
    return cast(M2tsScte35Control, data)
