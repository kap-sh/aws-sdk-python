"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnGroupColumnSchemaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.column_group_column_schema

ColumnGroupColumnSchemaList: TypeAlias = list[
    "capo_quicksight.types.column_group_column_schema.ColumnGroupColumnSchema"
]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnGroupColumnSchemaList) -> list:
    import capo_quicksight.types.column_group_column_schema

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.column_group_column_schema.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ColumnGroupColumnSchemaList:
    import capo_quicksight.types.column_group_column_schema

    out: ColumnGroupColumnSchemaList = []
    for item in data:
        out.append(
            capo_quicksight.types.column_group_column_schema.deserialize_json(item)
        )
    return out
