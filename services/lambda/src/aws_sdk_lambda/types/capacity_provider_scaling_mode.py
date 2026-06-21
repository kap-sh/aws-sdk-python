"""Generated from Smithy shape ``com.amazonaws.lambda#CapacityProviderScalingMode``."""

from typing import Literal, TypeAlias, cast

CapacityProviderScalingMode: TypeAlias = Literal[
    "Auto",
    "Manual",
]


# --- restJson1 ser/de ---
def serialize_json(value: CapacityProviderScalingMode) -> str:
    return value


def deserialize_json(data: str) -> CapacityProviderScalingMode:
    return cast(CapacityProviderScalingMode, data)
