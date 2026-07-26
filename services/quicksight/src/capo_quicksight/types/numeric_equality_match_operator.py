"""Generated from Smithy shape ``com.amazonaws.quicksight#NumericEqualityMatchOperator``."""

from typing import Literal, TypeAlias, cast

NumericEqualityMatchOperator: TypeAlias = Literal[
    "EQUALS",
    "DOES_NOT_EQUAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: NumericEqualityMatchOperator) -> str:
    return value


def deserialize_json(data: str) -> NumericEqualityMatchOperator:
    return cast(NumericEqualityMatchOperator, data)
