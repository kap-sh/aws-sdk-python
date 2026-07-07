"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnSchema``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.string


class ColumnSchema(TypedDict, closed=True):
    name: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The name of the column schema.</p>"""
    data_type: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The data type of the column schema.</p>"""
    geographic_role: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The geographic role of the column schema.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ColumnSchema) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "data_type" in value:
        out["DataType"] = value["data_type"]
    if "geographic_role" in value:
        out["GeographicRole"] = value["geographic_role"]
    return out


def deserialize_json(data: dict) -> ColumnSchema:
    out: ColumnSchema = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "DataType" in data:
        out["data_type"] = data["DataType"]
    if "GeographicRole" in data:
        out["geographic_role"] = data["GeographicRole"]
    return out
