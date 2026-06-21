"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetStatus``."""

from typing import Literal, TypeAlias, cast

DataSetStatus: TypeAlias = Literal[
    "CREATING",
    "UPDATING",
    "ACTIVE",
    "FAILED",
    "DELETING",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSetStatus) -> str:
    return value


def deserialize_json(data: str) -> DataSetStatus:
    return cast(DataSetStatus, data)
