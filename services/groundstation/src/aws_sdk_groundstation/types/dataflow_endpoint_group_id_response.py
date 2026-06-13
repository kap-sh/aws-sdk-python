"""Generated from Smithy shape ``com.amazonaws.groundstation#DataflowEndpointGroupIdResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.uuid


class DataflowEndpointGroupIdResponse(TypedDict):
    dataflow_endpoint_group_id: NotRequired["aws_sdk_groundstation.types.uuid.Uuid"]
    """<p>UUID of a dataflow endpoint group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataflowEndpointGroupIdResponse) -> dict:
    out: dict = {}
    if "dataflow_endpoint_group_id" in value:
        out["dataflowEndpointGroupId"] = value["dataflow_endpoint_group_id"]
    return out


def deserialize_json(data: dict) -> DataflowEndpointGroupIdResponse:
    out: DataflowEndpointGroupIdResponse = {}  # type: ignore[typeddict-item]
    if "dataflowEndpointGroupId" in data:
        out["dataflow_endpoint_group_id"] = data["dataflowEndpointGroupId"]
    return out
