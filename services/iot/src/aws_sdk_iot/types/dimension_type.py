"""Generated from Smithy shape ``com.amazonaws.iot#DimensionType``."""

from typing import Literal, TypeAlias, cast

DimensionType: TypeAlias = Literal["TOPIC_FILTER",]


# --- restJson1 ser/de ---
def serialize_json(value: DimensionType) -> str:
    return value


def deserialize_json(data: str) -> DimensionType:
    return cast(DimensionType, data)
