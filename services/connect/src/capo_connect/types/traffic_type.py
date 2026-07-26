"""Generated from Smithy shape ``com.amazonaws.connect#TrafficType``."""

from typing import Literal, TypeAlias, cast

TrafficType: TypeAlias = Literal[
    "GENERAL",
    "CAMPAIGN",
]


# --- restJson1 ser/de ---
def serialize_json(value: TrafficType) -> str:
    return value


def deserialize_json(data: str) -> TrafficType:
    return cast(TrafficType, data)
