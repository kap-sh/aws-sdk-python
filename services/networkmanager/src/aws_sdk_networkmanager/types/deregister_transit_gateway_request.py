"""Generated from Smithy shape ``com.amazonaws.networkmanager#DeregisterTransitGatewayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.global_network_id
    import aws_sdk_networkmanager.types.transit_gateway_arn


class DeregisterTransitGatewayRequest(TypedDict, closed=True):
    global_network_id: "aws_sdk_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network.</p>"""
    transit_gateway_arn: (
        "aws_sdk_networkmanager.types.transit_gateway_arn.TransitGatewayArn"
    )
    """<p>The Amazon Resource Name (ARN) of the transit gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeregisterTransitGatewayRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeregisterTransitGatewayRequest:
    out: DeregisterTransitGatewayRequest = {}  # type: ignore[typeddict-item]
    return out
