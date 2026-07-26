"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ColumnTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanroomsml.types.column_type

ColumnTypeList: TypeAlias = list["capo_cleanroomsml.types.column_type.ColumnType"]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnTypeList) -> list:
    import capo_cleanroomsml.types.column_type

    out: list = []
    for item in value:
        out.append(capo_cleanroomsml.types.column_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> ColumnTypeList:
    import capo_cleanroomsml.types.column_type

    out: ColumnTypeList = []
    for item in data:
        out.append(capo_cleanroomsml.types.column_type.deserialize_json(item))
    return out
