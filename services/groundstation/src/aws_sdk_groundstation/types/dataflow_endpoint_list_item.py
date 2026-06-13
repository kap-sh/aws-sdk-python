"""Generated from Smithy shape ``com.amazonaws.groundstation#DataflowEndpointListItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.dataflow_endpoint_group_arn
    import aws_sdk_groundstation.types.uuid


class DataflowEndpointListItem(TypedDict):
    dataflow_endpoint_group_id: NotRequired["aws_sdk_groundstation.types.uuid.Uuid"]
    """<p>UUID of a dataflow endpoint group.</p>"""
    dataflow_endpoint_group_arn: NotRequired[
        "aws_sdk_groundstation.types.dataflow_endpoint_group_arn.DataflowEndpointGroupArn"
    ]
    """<p>ARN of a dataflow endpoint group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataflowEndpointListItem) -> dict:
    out: dict = {}
    if "dataflow_endpoint_group_id" in value:
        out["dataflowEndpointGroupId"] = value["dataflow_endpoint_group_id"]
    if "dataflow_endpoint_group_arn" in value:
        out["dataflowEndpointGroupArn"] = value["dataflow_endpoint_group_arn"]
    return out


def deserialize_json(data: dict) -> DataflowEndpointListItem:
    out: DataflowEndpointListItem = {}  # type: ignore[typeddict-item]
    if "dataflowEndpointGroupId" in data:
        out["dataflow_endpoint_group_id"] = data["dataflowEndpointGroupId"]
    if "dataflowEndpointGroupArn" in data:
        out["dataflow_endpoint_group_arn"] = data["dataflowEndpointGroupArn"]
    return out
