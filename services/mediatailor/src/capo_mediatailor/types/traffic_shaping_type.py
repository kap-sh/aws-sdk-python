"""Generated from Smithy shape ``com.amazonaws.mediatailor#TrafficShapingType``."""

from typing import Literal, TypeAlias, cast

TrafficShapingType: TypeAlias = Literal[
    "RETRIEVAL_WINDOW",
    "TPS",
]


# --- restJson1 ser/de ---
def serialize_json(value: TrafficShapingType) -> str:
    return value


def deserialize_json(data: str) -> TrafficShapingType:
    return cast(TrafficShapingType, data)
