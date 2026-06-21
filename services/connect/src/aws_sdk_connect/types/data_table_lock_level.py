"""Generated from Smithy shape ``com.amazonaws.connect#DataTableLockLevel``."""

from typing import Literal, TypeAlias, cast

DataTableLockLevel: TypeAlias = Literal[
    "NONE",
    "DATA_TABLE",
    "PRIMARY_VALUE",
    "ATTRIBUTE",
    "VALUE",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataTableLockLevel) -> str:
    return value


def deserialize_json(data: str) -> DataTableLockLevel:
    return cast(DataTableLockLevel, data)
