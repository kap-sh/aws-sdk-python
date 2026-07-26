"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DataFormat``."""

from typing import Literal, TypeAlias, cast

DataFormat: TypeAlias = Literal[
    "CSV",
    "JSONL",
    "ORC",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataFormat) -> str:
    return value


def deserialize_json(data: str) -> DataFormat:
    return cast(DataFormat, data)
