"""Generated from Smithy shape ``com.amazonaws.connect#DescribeDataTableAttributeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.data_table_id
    import capo_connect.types.data_table_name
    import capo_connect.types.instance_id


class DescribeDataTableAttributeRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The unique identifier for the Amazon Connect instance.</p>"""
    data_table_id: "capo_connect.types.data_table_id.DataTableId"
    """<p>The unique identifier for the data table. Must also accept the table ARN with or without a version alias.</p>"""
    attribute_name: "capo_connect.types.data_table_name.DataTableName"
    """<p>The name of the attribute to retrieve detailed information for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDataTableAttributeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeDataTableAttributeRequest:
    out: DescribeDataTableAttributeRequest = {}  # type: ignore[typeddict-item]
    return out
