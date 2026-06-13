"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#Column``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bcm_data_exports.types.generic_string


class Column(TypedDict):
    name: NotRequired["aws_sdk_bcm_data_exports.types.generic_string.GenericString"]
    """<p>The column name.</p>"""
    type: NotRequired["aws_sdk_bcm_data_exports.types.generic_string.GenericString"]
    """<p>The kind of data a column stores.</p>"""
    description: NotRequired[
        "aws_sdk_bcm_data_exports.types.generic_string.GenericString"
    ]
    """<p>The description for a column.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Column) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        out["Type"] = value["type"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Column:
    out: Column = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
