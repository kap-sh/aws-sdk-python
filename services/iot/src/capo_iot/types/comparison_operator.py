"""Generated from Smithy shape ``com.amazonaws.iot#ComparisonOperator``."""

from typing import Literal, TypeAlias, cast

ComparisonOperator: TypeAlias = Literal[
    "less-than",
    "less-than-equals",
    "greater-than",
    "greater-than-equals",
    "in-cidr-set",
    "not-in-cidr-set",
    "in-port-set",
    "not-in-port-set",
    "in-set",
    "not-in-set",
]


# --- restJson1 ser/de ---
def serialize_json(value: ComparisonOperator) -> str:
    return value


def deserialize_json(data: str) -> ComparisonOperator:
    return cast(ComparisonOperator, data)
