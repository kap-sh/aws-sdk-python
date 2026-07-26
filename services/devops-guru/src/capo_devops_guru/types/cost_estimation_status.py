"""Generated from Smithy shape ``com.amazonaws.devopsguru#CostEstimationStatus``."""

from typing import Literal, TypeAlias, cast

CostEstimationStatus: TypeAlias = Literal[
    "ONGOING",
    "COMPLETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: CostEstimationStatus) -> str:
    return value


def deserialize_json(data: str) -> CostEstimationStatus:
    return cast(CostEstimationStatus, data)
