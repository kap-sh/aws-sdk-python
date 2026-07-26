"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelCustomization``."""

from typing import Literal, TypeAlias, cast

ModelCustomization: TypeAlias = Literal[
    "FINE_TUNING",
    "CONTINUED_PRE_TRAINING",
    "DISTILLATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: ModelCustomization) -> str:
    return value


def deserialize_json(data: str) -> ModelCustomization:
    return cast(ModelCustomization, data)
