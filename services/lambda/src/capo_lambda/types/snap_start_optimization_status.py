"""Generated from Smithy shape ``com.amazonaws.lambda#SnapStartOptimizationStatus``."""

from typing import Literal, TypeAlias, cast

SnapStartOptimizationStatus: TypeAlias = Literal[
    "On",
    "Off",
]


# --- restJson1 ser/de ---
def serialize_json(value: SnapStartOptimizationStatus) -> str:
    return value


def deserialize_json(data: str) -> SnapStartOptimizationStatus:
    return cast(SnapStartOptimizationStatus, data)
