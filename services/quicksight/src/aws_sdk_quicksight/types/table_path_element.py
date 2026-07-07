"""Generated from Smithy shape ``com.amazonaws.quicksight#TablePathElement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.table_path_element_id
    import aws_sdk_quicksight.types.table_path_element_name


class TablePathElement(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_quicksight.types.table_path_element_name.TablePathElementName"
    ]
    """<p>The name of the path element.</p>"""
    id: NotRequired["aws_sdk_quicksight.types.table_path_element_id.TablePathElementId"]
    """<p>The unique identifier of the path element.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TablePathElement) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_json(data: dict) -> TablePathElement:
    out: TablePathElement = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Id" in data:
        out["id"] = data["Id"]
    return out
