"""Generated from Smithy shape ``com.amazonaws.s3outposts#DeleteEndpointRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_s3outposts.types.endpoint_id
    import aws_sdk_s3outposts.types.outpost_id


class DeleteEndpointRequest(TypedDict):
    endpoint_id: "aws_sdk_s3outposts.types.endpoint_id.EndpointId"
    """<p>The ID of the endpoint.</p>"""
    outpost_id: "aws_sdk_s3outposts.types.outpost_id.OutpostId"
    """<p>The ID of the Outposts. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEndpointRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteEndpointRequest:
    out: DeleteEndpointRequest = {}  # type: ignore[typeddict-item]
    return out
