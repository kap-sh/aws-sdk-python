"""Generated from Smithy shape ``com.amazonaws.iotevents#ComparisonOperator``."""

from typing import Literal, TypeAlias, cast

ComparisonOperator: TypeAlias = Literal[
    "GREATER",
    "GREATER_OR_EQUAL",
    "LESS",
    "LESS_OR_EQUAL",
    "EQUAL",
    "NOT_EQUAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: ComparisonOperator) -> str:
    return value


def deserialize_json(data: str) -> ComparisonOperator:
    return cast(ComparisonOperator, data)
