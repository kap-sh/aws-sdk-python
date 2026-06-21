"""Generated from Smithy shape ``com.amazonaws.quicksight#DataLabelOverlap``."""

from typing import Literal, TypeAlias, cast

DataLabelOverlap: TypeAlias = Literal[
    "DISABLE_OVERLAP",
    "ENABLE_OVERLAP",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataLabelOverlap) -> str:
    return value


def deserialize_json(data: str) -> DataLabelOverlap:
    return cast(DataLabelOverlap, data)
