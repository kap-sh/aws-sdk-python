"""Generated from Smithy shape ``com.amazonaws.groundstation#DeleteDataflowEndpointGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.uuid


class DeleteDataflowEndpointGroupRequest(TypedDict, closed=True):
    dataflow_endpoint_group_id: "aws_sdk_groundstation.types.uuid.Uuid"
    """<p>UUID of a dataflow endpoint group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDataflowEndpointGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDataflowEndpointGroupRequest:
    out: DeleteDataflowEndpointGroupRequest = {}  # type: ignore[typeddict-item]
    return out
