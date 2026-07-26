"""Generated from Smithy shape ``com.amazonaws.quicksight#AxisBinding``."""

from typing import Literal, TypeAlias, cast

AxisBinding: TypeAlias = Literal[
    "PRIMARY_YAXIS",
    "SECONDARY_YAXIS",
]


# --- restJson1 ser/de ---
def serialize_json(value: AxisBinding) -> str:
    return value


def deserialize_json(data: str) -> AxisBinding:
    return cast(AxisBinding, data)
