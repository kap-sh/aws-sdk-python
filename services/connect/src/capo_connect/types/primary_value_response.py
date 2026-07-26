"""Generated from Smithy shape ``com.amazonaws.connect#PrimaryValueResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.data_table_id
    import capo_connect.types.data_table_name
    import capo_connect.types.string


class PrimaryValueResponse(TypedDict, closed=True):
    attribute_name: NotRequired["capo_connect.types.data_table_name.DataTableName"]
    """<p>The value's attribute name.</p>"""
    attribute_id: NotRequired["capo_connect.types.data_table_id.DataTableId"]
    """<p>The value's attribute ID.</p>"""
    value: NotRequired["capo_connect.types.string.String"]
    """<p>The value's value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrimaryValueResponse) -> dict:
    out: dict = {}
    if "attribute_name" in value:
        out["AttributeName"] = value["attribute_name"]
    if "attribute_id" in value:
        out["AttributeId"] = value["attribute_id"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> PrimaryValueResponse:
    out: PrimaryValueResponse = {}  # type: ignore[typeddict-item]
    if "AttributeName" in data:
        out["attribute_name"] = data["AttributeName"]
    if "AttributeId" in data:
        out["attribute_id"] = data["AttributeId"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
