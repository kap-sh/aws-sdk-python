"""Generated from Smithy shape ``com.amazonaws.quicksight#DataLabelContent``."""

from typing import Literal, TypeAlias, cast

DataLabelContent: TypeAlias = Literal[
    "VALUE",
    "PERCENT",
    "VALUE_AND_PERCENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataLabelContent) -> str:
    return value


def deserialize_json(data: str) -> DataLabelContent:
    return cast(DataLabelContent, data)
