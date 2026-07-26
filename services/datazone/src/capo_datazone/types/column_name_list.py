"""Generated from Smithy shape ``com.amazonaws.datazone#ColumnNameList``."""

from typing import TypeAlias

ColumnNameList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> ColumnNameList:
    return list(data)
