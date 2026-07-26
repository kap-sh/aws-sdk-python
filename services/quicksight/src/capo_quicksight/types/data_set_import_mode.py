"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetImportMode``."""

from typing import Literal, TypeAlias, cast

DataSetImportMode: TypeAlias = Literal[
    "SPICE",
    "DIRECT_QUERY",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSetImportMode) -> str:
    return value


def deserialize_json(data: str) -> DataSetImportMode:
    return cast(DataSetImportMode, data)
