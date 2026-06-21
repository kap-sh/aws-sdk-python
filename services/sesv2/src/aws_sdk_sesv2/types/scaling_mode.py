"""Generated from Smithy shape ``com.amazonaws.sesv2#ScalingMode``."""

from typing import Literal, TypeAlias, cast

ScalingMode: TypeAlias = Literal[
    "STANDARD",
    "MANAGED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ScalingMode) -> str:
    return value


def deserialize_json(data: str) -> ScalingMode:
    return cast(ScalingMode, data)
