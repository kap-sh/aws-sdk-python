"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnToUnpivot``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.cell_value
    import capo_quicksight.types.column_name


class ColumnToUnpivot(TypedDict, closed=True):
    column_name: NotRequired["capo_quicksight.types.column_name.ColumnName"]
    """<p>The name of the column to unpivot from the source data.</p>"""
    new_value: NotRequired["capo_quicksight.types.cell_value.CellValue"]
    """<p>The value to assign to this column in the unpivoted result, typically the column name or a descriptive label.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ColumnToUnpivot) -> dict:
    out: dict = {}
    if "column_name" in value:
        out["ColumnName"] = value["column_name"]
    if "new_value" in value:
        out["NewValue"] = value["new_value"]
    return out


def deserialize_json(data: dict) -> ColumnToUnpivot:
    out: ColumnToUnpivot = {}  # type: ignore[typeddict-item]
    if "ColumnName" in data:
        out["column_name"] = data["ColumnName"]
    if "NewValue" in data:
        out["new_value"] = data["NewValue"]
    return out
