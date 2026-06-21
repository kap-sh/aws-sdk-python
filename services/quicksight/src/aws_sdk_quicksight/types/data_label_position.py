"""Generated from Smithy shape ``com.amazonaws.quicksight#DataLabelPosition``."""

from typing import Literal, TypeAlias, cast

DataLabelPosition: TypeAlias = Literal[
    "INSIDE",
    "OUTSIDE",
    "LEFT",
    "TOP",
    "BOTTOM",
    "RIGHT",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataLabelPosition) -> str:
    return value


def deserialize_json(data: str) -> DataLabelPosition:
    return cast(DataLabelPosition, data)
