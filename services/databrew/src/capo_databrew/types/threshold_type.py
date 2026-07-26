"""Generated from Smithy shape ``com.amazonaws.databrew#ThresholdType``."""

from typing import Literal, TypeAlias, cast

ThresholdType: TypeAlias = Literal[
    "GREATER_THAN_OR_EQUAL",
    "LESS_THAN_OR_EQUAL",
    "GREATER_THAN",
    "LESS_THAN",
]


# --- restJson1 ser/de ---
def serialize_json(value: ThresholdType) -> str:
    return value


def deserialize_json(data: str) -> ThresholdType:
    return cast(ThresholdType, data)
