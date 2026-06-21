"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AggregateType``."""

from typing import Literal, TypeAlias, cast

AggregateType: TypeAlias = Literal[
    "AVERAGE",
    "COUNT",
    "MAXIMUM",
    "MINIMUM",
    "SUM",
    "STANDARD_DEVIATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: AggregateType) -> str:
    return value


def deserialize_json(data: str) -> AggregateType:
    return cast(AggregateType, data)
