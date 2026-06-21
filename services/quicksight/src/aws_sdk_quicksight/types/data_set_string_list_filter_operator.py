"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetStringListFilterOperator``."""

from typing import Literal, TypeAlias, cast

DataSetStringListFilterOperator: TypeAlias = Literal[
    "INCLUDE",
    "EXCLUDE",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSetStringListFilterOperator) -> str:
    return value


def deserialize_json(data: str) -> DataSetStringListFilterOperator:
    return cast(DataSetStringListFilterOperator, data)
