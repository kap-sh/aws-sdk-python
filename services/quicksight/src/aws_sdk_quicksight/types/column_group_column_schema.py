"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnGroupColumnSchema``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.string


class ColumnGroupColumnSchema(TypedDict):
    name: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The name of the column group's column schema.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ColumnGroupColumnSchema) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> ColumnGroupColumnSchema:
    out: ColumnGroupColumnSchema = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
