"""Generated from Smithy shape ``com.amazonaws.quicksight#AppendedColumn``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.column_id
    import aws_sdk_quicksight.types.column_name


class AppendedColumn(TypedDict):
    column_name: "aws_sdk_quicksight.types.column_name.ColumnName"
    """<p>The name of the column to include in the appended result.</p>"""
    new_column_id: "aws_sdk_quicksight.types.column_id.ColumnId"
    """<p>A unique identifier for the column in the appended result.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppendedColumn) -> dict:
    out: dict = {}
    out["ColumnName"] = value["column_name"]
    out["NewColumnId"] = value["new_column_id"]
    return out


def deserialize_json(data: dict) -> AppendedColumn:
    out: AppendedColumn = {}  # type: ignore[typeddict-item]
    if "ColumnName" in data:
        out["column_name"] = data["ColumnName"]
    else:
        raise DeserializationError("AppendedColumn.column_name required")
    if "NewColumnId" in data:
        out["new_column_id"] = data["NewColumnId"]
    else:
        raise DeserializationError("AppendedColumn.new_column_id required")
    return out
