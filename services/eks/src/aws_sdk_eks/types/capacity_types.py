"""Generated from Smithy shape ``com.amazonaws.eks#CapacityTypes``."""

from typing import Literal, TypeAlias, cast

CapacityTypes: TypeAlias = Literal[
    "ON_DEMAND",
    "SPOT",
    "CAPACITY_BLOCK",
]


# --- restJson1 ser/de ---
def serialize_json(value: CapacityTypes) -> str:
    return value


def deserialize_json(data: str) -> CapacityTypes:
    return cast(CapacityTypes, data)
