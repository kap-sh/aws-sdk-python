"""Generated from Smithy shape ``com.amazonaws.mediaconnect#FlowSize``."""

from typing import Literal, TypeAlias, cast

FlowSize: TypeAlias = Literal[
    "MEDIUM",
    "LARGE",
    "LARGE_4X",
]


# --- restJson1 ser/de ---
def serialize_json(value: FlowSize) -> str:
    return value


def deserialize_json(data: str) -> FlowSize:
    return cast(FlowSize, data)
