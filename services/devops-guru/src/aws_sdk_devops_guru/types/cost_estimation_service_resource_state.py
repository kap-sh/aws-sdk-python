"""Generated from Smithy shape ``com.amazonaws.devopsguru#CostEstimationServiceResourceState``."""

from typing import Literal, TypeAlias, cast

CostEstimationServiceResourceState: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: CostEstimationServiceResourceState) -> str:
    return value


def deserialize_json(data: str) -> CostEstimationServiceResourceState:
    return cast(CostEstimationServiceResourceState, data)
