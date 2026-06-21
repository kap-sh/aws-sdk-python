"""Generated from Smithy shape ``com.amazonaws.iot#BehaviorCriteriaType``."""

from typing import Literal, TypeAlias, cast

BehaviorCriteriaType: TypeAlias = Literal[
    "STATIC",
    "STATISTICAL",
    "MACHINE_LEARNING",
]


# --- restJson1 ser/de ---
def serialize_json(value: BehaviorCriteriaType) -> str:
    return value


def deserialize_json(data: str) -> BehaviorCriteriaType:
    return cast(BehaviorCriteriaType, data)
