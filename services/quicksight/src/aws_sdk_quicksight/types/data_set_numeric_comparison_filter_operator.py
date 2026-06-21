"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetNumericComparisonFilterOperator``."""

from typing import Literal, TypeAlias, cast

DataSetNumericComparisonFilterOperator: TypeAlias = Literal[
    "EQUALS",
    "DOES_NOT_EQUAL",
    "GREATER_THAN",
    "GREATER_THAN_OR_EQUALS_TO",
    "LESS_THAN",
    "LESS_THAN_OR_EQUALS_TO",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSetNumericComparisonFilterOperator) -> str:
    return value


def deserialize_json(data: str) -> DataSetNumericComparisonFilterOperator:
    return cast(DataSetNumericComparisonFilterOperator, data)
