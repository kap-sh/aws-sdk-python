"""Generated from Smithy shape ``com.amazonaws.connect#DeleteDataTableAttributeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.data_table_id
    import aws_sdk_connect.types.data_table_name
    import aws_sdk_connect.types.instance_id


class DeleteDataTableAttributeRequest(TypedDict, closed=True):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The unique identifier for the Amazon Connect instance.</p>"""
    data_table_id: "aws_sdk_connect.types.data_table_id.DataTableId"
    """<p>The unique identifier for the data table.</p>"""
    attribute_name: "aws_sdk_connect.types.data_table_name.DataTableName"
    """<p>The name of the attribute to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDataTableAttributeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDataTableAttributeRequest:
    out: DeleteDataTableAttributeRequest = {}  # type: ignore[typeddict-item]
    return out
