"""Generated from Smithy shape ``com.amazonaws.databrew#ColumnSelector``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_databrew.types.column_name


class ColumnSelector(TypedDict):
    regex: NotRequired["aws_sdk_databrew.types.column_name.ColumnName"]
    """<p>A regular expression for selecting a column from a dataset.</p>"""
    name: NotRequired["aws_sdk_databrew.types.column_name.ColumnName"]
    """<p>The name of a column from a dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ColumnSelector) -> dict:
    out: dict = {}
    if "regex" in value:
        out["Regex"] = value["regex"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> ColumnSelector:
    out: ColumnSelector = {}  # type: ignore[typeddict-item]
    if "Regex" in data:
        out["regex"] = data["Regex"]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
