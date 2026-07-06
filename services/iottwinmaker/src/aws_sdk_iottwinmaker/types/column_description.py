"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ColumnDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.column_name
    import aws_sdk_iottwinmaker.types.column_type


class ColumnDescription(TypedDict, closed=True):
    name: NotRequired["aws_sdk_iottwinmaker.types.column_name.ColumnName"]
    """<p>The name of the column description.</p>"""
    type: NotRequired["aws_sdk_iottwinmaker.types.column_type.ColumnType"]
    """<p>The type of the column description.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ColumnDescription) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "type" in value:
        out["type"] = value["type"]
    return out


def deserialize_json(data: dict) -> ColumnDescription:
    out: ColumnDescription = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "type" in data:
        out["type"] = data["type"]
    return out
