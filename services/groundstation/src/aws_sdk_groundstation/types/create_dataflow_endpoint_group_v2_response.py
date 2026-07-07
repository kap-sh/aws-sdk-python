"""Generated from Smithy shape ``com.amazonaws.groundstation#CreateDataflowEndpointGroupV2Response``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.uuid


class CreateDataflowEndpointGroupV2Response(TypedDict, closed=True):
    dataflow_endpoint_group_id: NotRequired["aws_sdk_groundstation.types.uuid.Uuid"]
    """<p>Dataflow endpoint group ID</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataflowEndpointGroupV2Response) -> dict:
    out: dict = {}
    if "dataflow_endpoint_group_id" in value:
        out["dataflowEndpointGroupId"] = value["dataflow_endpoint_group_id"]
    return out


def deserialize_json(data: dict) -> CreateDataflowEndpointGroupV2Response:
    out: CreateDataflowEndpointGroupV2Response = {}  # type: ignore[typeddict-item]
    if "dataflowEndpointGroupId" in data:
        out["dataflow_endpoint_group_id"] = data["dataflowEndpointGroupId"]
    return out
