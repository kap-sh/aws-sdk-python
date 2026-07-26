"""Generated from Smithy shape ``com.amazonaws.databrew#ThresholdUnit``."""

from typing import Literal, TypeAlias, cast

ThresholdUnit: TypeAlias = Literal[
    "COUNT",
    "PERCENTAGE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ThresholdUnit) -> str:
    return value


def deserialize_json(data: str) -> ThresholdUnit:
    return cast(ThresholdUnit, data)
