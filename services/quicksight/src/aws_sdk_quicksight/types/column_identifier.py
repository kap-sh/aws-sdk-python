"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.column_name
    import aws_sdk_quicksight.types.data_set_identifier


class ColumnIdentifier(TypedDict, closed=True):
    data_set_identifier: (
        "aws_sdk_quicksight.types.data_set_identifier.DataSetIdentifier"
    )
    """<p>The data set that the column belongs to.</p>"""
    column_name: "aws_sdk_quicksight.types.column_name.ColumnName"
    """<p>The name of the column.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ColumnIdentifier) -> dict:
    out: dict = {}
    out["DataSetIdentifier"] = value["data_set_identifier"]
    out["ColumnName"] = value["column_name"]
    return out


def deserialize_json(data: dict) -> ColumnIdentifier:
    out: ColumnIdentifier = {}  # type: ignore[typeddict-item]
    if "DataSetIdentifier" in data:
        out["data_set_identifier"] = data["DataSetIdentifier"]
    else:
        raise DeserializationError("ColumnIdentifier.data_set_identifier required")
    if "ColumnName" in data:
        out["column_name"] = data["ColumnName"]
    else:
        raise DeserializationError("ColumnIdentifier.column_name required")
    return out
