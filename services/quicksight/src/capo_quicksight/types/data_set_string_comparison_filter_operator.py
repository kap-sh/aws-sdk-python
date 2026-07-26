"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetStringComparisonFilterOperator``."""

from typing import Literal, TypeAlias, cast

DataSetStringComparisonFilterOperator: TypeAlias = Literal[
    "EQUALS",
    "DOES_NOT_EQUAL",
    "CONTAINS",
    "DOES_NOT_CONTAIN",
    "STARTS_WITH",
    "ENDS_WITH",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSetStringComparisonFilterOperator) -> str:
    return value


def deserialize_json(data: str) -> DataSetStringComparisonFilterOperator:
    return cast(DataSetStringComparisonFilterOperator, data)
