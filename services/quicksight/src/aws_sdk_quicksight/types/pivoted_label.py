"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotedLabel``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.cell_value
    import aws_sdk_quicksight.types.column_id
    import aws_sdk_quicksight.types.column_name


class PivotedLabel(TypedDict, closed=True):
    label_name: "aws_sdk_quicksight.types.cell_value.CellValue"
    """<p>The label value from the source data to be pivoted.</p>"""
    new_column_name: "aws_sdk_quicksight.types.column_name.ColumnName"
    """<p>The name for the new column created from this pivoted label.</p>"""
    new_column_id: "aws_sdk_quicksight.types.column_id.ColumnId"
    """<p>A unique identifier for the new column created from this pivoted label.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PivotedLabel) -> dict:
    out: dict = {}
    out["LabelName"] = value["label_name"]
    out["NewColumnName"] = value["new_column_name"]
    out["NewColumnId"] = value["new_column_id"]
    return out


def deserialize_json(data: dict) -> PivotedLabel:
    out: PivotedLabel = {}  # type: ignore[typeddict-item]
    if "LabelName" in data:
        out["label_name"] = data["LabelName"]
    else:
        raise DeserializationError("PivotedLabel.label_name required")
    if "NewColumnName" in data:
        out["new_column_name"] = data["NewColumnName"]
    else:
        raise DeserializationError("PivotedLabel.new_column_name required")
    if "NewColumnId" in data:
        out["new_column_id"] = data["NewColumnId"]
    else:
        raise DeserializationError("PivotedLabel.new_column_id required")
    return out
