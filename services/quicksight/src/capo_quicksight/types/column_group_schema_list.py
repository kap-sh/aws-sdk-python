"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnGroupSchemaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.column_group_schema

ColumnGroupSchemaList: TypeAlias = list[
    "capo_quicksight.types.column_group_schema.ColumnGroupSchema"
]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnGroupSchemaList) -> list:
    import capo_quicksight.types.column_group_schema

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.column_group_schema.serialize_json(item))
    return out


def deserialize_json(data: list) -> ColumnGroupSchemaList:
    import capo_quicksight.types.column_group_schema

    out: ColumnGroupSchemaList = []
    for item in data:
        out.append(capo_quicksight.types.column_group_schema.deserialize_json(item))
    return out
