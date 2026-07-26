"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#FilterOperator``."""

from typing import Literal, TypeAlias, cast

FilterOperator: TypeAlias = Literal[
    "Equals",
    "NotEquals",
    "GreaterThan",
    "LessThan",
    "GreaterThanOrEqual",
    "LessThanOrEqual",
    "Contains",
    "NotContains",
]


# --- restJson1 ser/de ---
def serialize_json(value: FilterOperator) -> str:
    return value


def deserialize_json(data: str) -> FilterOperator:
    return cast(FilterOperator, data)
