"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnSchemaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.column_schema

ColumnSchemaList: TypeAlias = list["capo_quicksight.types.column_schema.ColumnSchema"]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnSchemaList) -> list:
    import capo_quicksight.types.column_schema

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.column_schema.serialize_json(item))
    return out


def deserialize_json(data: list) -> ColumnSchemaList:
    import capo_quicksight.types.column_schema

    out: ColumnSchemaList = []
    for item in data:
        out.append(capo_quicksight.types.column_schema.deserialize_json(item))
    return out
