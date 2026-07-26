"""Generated from Smithy shape ``com.amazonaws.deadline#LogicalOperator``."""

from typing import Literal, TypeAlias, cast

LogicalOperator: TypeAlias = Literal[
    "AND",
    "OR",
]


# --- restJson1 ser/de ---
def serialize_json(value: LogicalOperator) -> str:
    return value


def deserialize_json(data: str) -> LogicalOperator:
    return cast(LogicalOperator, data)
