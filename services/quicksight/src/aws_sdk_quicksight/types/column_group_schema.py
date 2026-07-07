"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnGroupSchema``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.column_group_column_schema_list
    import aws_sdk_quicksight.types.string


class ColumnGroupSchema(TypedDict, closed=True):
    name: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The name of the column group schema.</p>"""
    column_group_column_schema_list: NotRequired[
        "aws_sdk_quicksight.types.column_group_column_schema_list.ColumnGroupColumnSchemaList"
    ]
    """<p>A structure containing the list of schemas for column group columns.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ColumnGroupSchema) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "column_group_column_schema_list" in value:
        import aws_sdk_quicksight.types.column_group_column_schema_list

        out["ColumnGroupColumnSchemaList"] = (
            aws_sdk_quicksight.types.column_group_column_schema_list.serialize_json(
                value["column_group_column_schema_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ColumnGroupSchema:
    out: ColumnGroupSchema = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "ColumnGroupColumnSchemaList" in data:
        import aws_sdk_quicksight.types.column_group_column_schema_list

        out["column_group_column_schema_list"] = (
            aws_sdk_quicksight.types.column_group_column_schema_list.deserialize_json(
                data["ColumnGroupColumnSchemaList"]
            )
        )
    return out
