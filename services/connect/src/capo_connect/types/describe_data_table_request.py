"""Generated from Smithy shape ``com.amazonaws.connect#DescribeDataTableRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.data_table_id
    import capo_connect.types.instance_id


class DescribeDataTableRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The unique identifier for the Amazon Connect instance.</p>"""
    data_table_id: "capo_connect.types.data_table_id.DataTableId"
    """<p>The unique identifier for the data table. Must also accept the table ARN with or without a version alias. If no alias is provided, the default behavior is identical to providing the $LATEST alias.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDataTableRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeDataTableRequest:
    out: DescribeDataTableRequest = {}  # type: ignore[typeddict-item]
    return out
