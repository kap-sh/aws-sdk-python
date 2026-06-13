"""Generated from Smithy shape ``com.amazonaws.rtbfabric#GetRequesterGatewayRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rtbfabric.types.gateway_id


class GetRequesterGatewayRequest(TypedDict):
    gateway_id: "aws_sdk_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRequesterGatewayRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRequesterGatewayRequest:
    out: GetRequesterGatewayRequest = {}  # type: ignore[typeddict-item]
    return out
