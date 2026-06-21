"""Generated from Smithy shape ``com.amazonaws.customerprofiles#logicalOperator``."""

from typing import Literal, TypeAlias, cast

logicalOperator: TypeAlias = Literal[
    "AND",
    "OR",
]


# --- restJson1 ser/de ---
def serialize_json(value: logicalOperator) -> str:
    return value


def deserialize_json(data: str) -> logicalOperator:
    return cast(logicalOperator, data)
