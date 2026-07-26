"""Generated from Smithy shape ``com.amazonaws.quicksight#ComparisonOperator``."""

from typing import Literal, TypeAlias, cast

ComparisonOperator: TypeAlias = Literal[
    "StringEquals",
    "StringLike",
]


# --- restJson1 ser/de ---
def serialize_json(value: ComparisonOperator) -> str:
    return value


def deserialize_json(data: str) -> ComparisonOperator:
    return cast(ComparisonOperator, data)
