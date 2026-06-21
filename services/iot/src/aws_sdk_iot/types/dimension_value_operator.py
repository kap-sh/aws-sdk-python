"""Generated from Smithy shape ``com.amazonaws.iot#DimensionValueOperator``."""

from typing import Literal, TypeAlias, cast

DimensionValueOperator: TypeAlias = Literal[
    "IN",
    "NOT_IN",
]


# --- restJson1 ser/de ---
def serialize_json(value: DimensionValueOperator) -> str:
    return value


def deserialize_json(data: str) -> DimensionValueOperator:
    return cast(DimensionValueOperator, data)
