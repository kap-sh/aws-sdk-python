"""Generated from Smithy shape ``com.amazonaws.finspacedata#SchemaDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.column_list
    import aws_sdk_finspace_data.types.column_name_list


class SchemaDefinition(TypedDict, closed=True):
    columns: NotRequired["aws_sdk_finspace_data.types.column_list.ColumnList"]
    """<p>List of column definitions.</p>"""
    primary_key_columns: NotRequired[
        "aws_sdk_finspace_data.types.column_name_list.ColumnNameList"
    ]
    """<p>List of column names used for primary key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SchemaDefinition) -> dict:
    out: dict = {}
    if "columns" in value:
        import aws_sdk_finspace_data.types.column_list

        out["columns"] = aws_sdk_finspace_data.types.column_list.serialize_json(
            value["columns"]
        )
    if "primary_key_columns" in value:
        import aws_sdk_finspace_data.types.column_name_list

        out["primaryKeyColumns"] = (
            aws_sdk_finspace_data.types.column_name_list.serialize_json(
                value["primary_key_columns"]
            )
        )
    return out


def deserialize_json(data: dict) -> SchemaDefinition:
    out: SchemaDefinition = {}  # type: ignore[typeddict-item]
    if "columns" in data:
        import aws_sdk_finspace_data.types.column_list

        out["columns"] = aws_sdk_finspace_data.types.column_list.deserialize_json(
            data["columns"]
        )
    if "primaryKeyColumns" in data:
        import aws_sdk_finspace_data.types.column_name_list

        out["primary_key_columns"] = (
            aws_sdk_finspace_data.types.column_name_list.deserialize_json(
                data["primaryKeyColumns"]
            )
        )
    return out
