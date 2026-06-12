"""Generated from Smithy shape ``com.amazonaws.dsql#GetVpcEndpointServiceNameInput``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_dsql.types.cluster_id

class GetVpcEndpointServiceNameInput(TypedDict):
    identifier: "aws_sdk_dsql.types.cluster_id.ClusterId"
    """<p>The ID of the cluster to retrieve.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: GetVpcEndpointServiceNameInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetVpcEndpointServiceNameInput:
    out: GetVpcEndpointServiceNameInput = {}  # type: ignore[typeddict-item]
    return out