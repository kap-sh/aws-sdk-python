"""Generated from Smithy shape ``com.amazonaws.bedrock#CustomizationType``."""

from typing import Literal, TypeAlias, cast

CustomizationType: TypeAlias = Literal[
    "FINE_TUNING",
    "CONTINUED_PRE_TRAINING",
    "DISTILLATION",
    "REINFORCEMENT_FINE_TUNING",
    "IMPORTED",
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomizationType) -> str:
    return value


def deserialize_json(data: str) -> CustomizationType:
    return cast(CustomizationType, data)
