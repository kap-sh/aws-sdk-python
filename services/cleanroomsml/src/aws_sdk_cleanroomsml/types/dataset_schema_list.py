"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#DatasetSchemaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.column_schema

DatasetSchemaList: TypeAlias = list[
    "aws_sdk_cleanroomsml.types.column_schema.ColumnSchema"
]


# --- restJson1 ser/de ---
def serialize_json(value: DatasetSchemaList) -> list:
    import aws_sdk_cleanroomsml.types.column_schema

    out: list = []
    for item in value:
        out.append(aws_sdk_cleanroomsml.types.column_schema.serialize_json(item))
    return out


def deserialize_json(data: list) -> DatasetSchemaList:
    import aws_sdk_cleanroomsml.types.column_schema

    out: DatasetSchemaList = []
    for item in data:
        out.append(aws_sdk_cleanroomsml.types.column_schema.deserialize_json(item))
    return out
