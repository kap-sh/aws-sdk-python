"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#DimensionLabelType``."""

from typing import Literal, TypeAlias, cast

DimensionLabelType: TypeAlias = Literal[
    "Region",
    "SagemakerOption",
]


# --- restJson1 ser/de ---
def serialize_json(value: DimensionLabelType) -> str:
    return value


def deserialize_json(data: str) -> DimensionLabelType:
    return cast(DimensionLabelType, data)
