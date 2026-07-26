"""Generated from Smithy shape ``com.amazonaws.quicksight#RenameColumnOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.column_name


class RenameColumnOperation(TypedDict, closed=True):
    column_name: "capo_quicksight.types.column_name.ColumnName"
    """<p>The name of the column to be renamed.</p>"""
    new_column_name: "capo_quicksight.types.column_name.ColumnName"
    """<p>The new name for the column.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RenameColumnOperation) -> dict:
    out: dict = {}
    out["ColumnName"] = value["column_name"]
    out["NewColumnName"] = value["new_column_name"]
    return out


def deserialize_json(data: dict) -> RenameColumnOperation:
    out: RenameColumnOperation = {}  # type: ignore[typeddict-item]
    if "ColumnName" in data:
        out["column_name"] = data["ColumnName"]
    else:
        raise DeserializationError("RenameColumnOperation.column_name required")
    if "NewColumnName" in data:
        out["new_column_name"] = data["NewColumnName"]
    else:
        raise DeserializationError("RenameColumnOperation.new_column_name required")
    return out
