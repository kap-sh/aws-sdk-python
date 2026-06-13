"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ColumnTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.column_type

ColumnTypeList: TypeAlias = list["aws_sdk_cleanroomsml.types.column_type.ColumnType"]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnTypeList) -> list:
    import aws_sdk_cleanroomsml.types.column_type

    out: list = []
    for item in value:
        out.append(aws_sdk_cleanroomsml.types.column_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> ColumnTypeList:
    import aws_sdk_cleanroomsml.types.column_type

    out: ColumnTypeList = []
    for item in data:
        out.append(aws_sdk_cleanroomsml.types.column_type.deserialize_json(item))
    return out
