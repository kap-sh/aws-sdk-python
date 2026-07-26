"""Generated from Smithy shape ``com.amazonaws.mpa#Operator``."""

from typing import Literal, TypeAlias, cast

Operator: TypeAlias = Literal[
    "EQ",
    "NE",
    "GT",
    "LT",
    "GTE",
    "LTE",
    "CONTAINS",
    "NOT_CONTAINS",
    "BETWEEN",
]


# --- restJson1 ser/de ---
def serialize_json(value: Operator) -> str:
    return value


def deserialize_json(data: str) -> Operator:
    return cast(Operator, data)
