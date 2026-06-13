"""Generated from Smithy shape ``com.amazonaws.quicksight#OutputColumnNameOverride``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.column_name


class OutputColumnNameOverride(TypedDict):
    source_column_name: NotRequired["aws_sdk_quicksight.types.column_name.ColumnName"]
    """<p>The original name of the column from the source transform operation.</p>"""
    output_column_name: "aws_sdk_quicksight.types.column_name.ColumnName"
    """<p>The new name to assign to the column in the output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutputColumnNameOverride) -> dict:
    out: dict = {}
    if "source_column_name" in value:
        out["SourceColumnName"] = value["source_column_name"]
    out["OutputColumnName"] = value["output_column_name"]
    return out


def deserialize_json(data: dict) -> OutputColumnNameOverride:
    out: OutputColumnNameOverride = {}  # type: ignore[typeddict-item]
    if "SourceColumnName" in data:
        out["source_column_name"] = data["SourceColumnName"]
    if "OutputColumnName" in data:
        out["output_column_name"] = data["OutputColumnName"]
    else:
        raise DeserializationError(
            "OutputColumnNameOverride.output_column_name required"
        )
    return out
