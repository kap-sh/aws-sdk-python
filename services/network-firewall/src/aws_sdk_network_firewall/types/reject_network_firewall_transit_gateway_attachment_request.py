"""Generated from Smithy shape ``com.amazonaws.networkfirewall#RejectNetworkFirewallTransitGatewayAttachmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.transit_gateway_attachment_id


class RejectNetworkFirewallTransitGatewayAttachmentRequest(TypedDict, closed=True):
    transit_gateway_attachment_id: "aws_sdk_network_firewall.types.transit_gateway_attachment_id.TransitGatewayAttachmentId"
    """<p>Required. The unique identifier of the transit gateway attachment to reject. This ID is returned in the response when creating a transit gateway-attached firewall.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: RejectNetworkFirewallTransitGatewayAttachmentRequest,
) -> dict:
    out: dict = {}
    out["TransitGatewayAttachmentId"] = value["transit_gateway_attachment_id"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> RejectNetworkFirewallTransitGatewayAttachmentRequest:
    out: RejectNetworkFirewallTransitGatewayAttachmentRequest = {}  # type: ignore[typeddict-item]
    if "TransitGatewayAttachmentId" in data:
        out["transit_gateway_attachment_id"] = data["TransitGatewayAttachmentId"]
    else:
        raise DeserializationError(
            "RejectNetworkFirewallTransitGatewayAttachmentRequest.transit_gateway_attachment_id required"
        )
    return out
