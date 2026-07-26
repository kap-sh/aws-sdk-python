"""Generated from Smithy shape ``com.amazonaws.resiliencehub#EstimatedCostTier``."""

from typing import Literal, TypeAlias, cast

EstimatedCostTier: TypeAlias = Literal[
    "L1",
    "L2",
    "L3",
    "L4",
]


# --- restJson1 ser/de ---
def serialize_json(value: EstimatedCostTier) -> str:
    return value


def deserialize_json(data: str) -> EstimatedCostTier:
    return cast(EstimatedCostTier, data)
