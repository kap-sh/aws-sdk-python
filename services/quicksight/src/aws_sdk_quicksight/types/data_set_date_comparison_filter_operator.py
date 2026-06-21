"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetDateComparisonFilterOperator``."""

from typing import Literal, TypeAlias, cast

DataSetDateComparisonFilterOperator: TypeAlias = Literal[
    "BEFORE",
    "BEFORE_OR_EQUALS_TO",
    "AFTER",
    "AFTER_OR_EQUALS_TO",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSetDateComparisonFilterOperator) -> str:
    return value


def deserialize_json(data: str) -> DataSetDateComparisonFilterOperator:
    return cast(DataSetDateComparisonFilterOperator, data)
