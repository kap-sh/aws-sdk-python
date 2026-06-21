"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Operator``."""

from typing import Literal, TypeAlias, cast

Operator: TypeAlias = Literal[
    "EQUAL_TO",
    "GREATER_THAN",
    "LESS_THAN",
    "NOT_EQUAL_TO",
]


# --- restJson1 ser/de ---
def serialize_json(value: Operator) -> str:
    return value


def deserialize_json(data: str) -> Operator:
    return cast(Operator, data)
