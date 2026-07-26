"""Generated from Smithy shape ``com.amazonaws.opensearch#DeleteVpcEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.vpc_endpoint_id


class DeleteVpcEndpointRequest(TypedDict, closed=True):
    vpc_endpoint_id: "capo_opensearch.types.vpc_endpoint_id.VpcEndpointId"
    """<p>The unique identifier of the endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteVpcEndpointRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteVpcEndpointRequest:
    out: DeleteVpcEndpointRequest = {}  # type: ignore[typeddict-item]
    return out
