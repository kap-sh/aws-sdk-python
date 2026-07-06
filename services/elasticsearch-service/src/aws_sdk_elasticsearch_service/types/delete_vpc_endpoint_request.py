"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DeleteVpcEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.vpc_endpoint_id


class DeleteVpcEndpointRequest(TypedDict, closed=True):
    vpc_endpoint_id: "aws_sdk_elasticsearch_service.types.vpc_endpoint_id.VpcEndpointId"
    """<p>The unique identifier of the endpoint to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteVpcEndpointRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteVpcEndpointRequest:
    out: DeleteVpcEndpointRequest = {}  # type: ignore[typeddict-item]
    return out
