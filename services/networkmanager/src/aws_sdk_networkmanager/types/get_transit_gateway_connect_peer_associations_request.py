"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetTransitGatewayConnectPeerAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.global_network_id
    import aws_sdk_networkmanager.types.max_results
    import aws_sdk_networkmanager.types.next_token
    import aws_sdk_networkmanager.types.transit_gateway_connect_peer_arn_list


class GetTransitGatewayConnectPeerAssociationsRequest(TypedDict, closed=True):
    global_network_id: "aws_sdk_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network.</p>"""
    transit_gateway_connect_peer_arns: NotRequired[
        "aws_sdk_networkmanager.types.transit_gateway_connect_peer_arn_list.TransitGatewayConnectPeerArnList"
    ]
    """<p>One or more transit gateway Connect peer Amazon Resource Names (ARNs).</p>"""
    max_results: NotRequired["aws_sdk_networkmanager.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["aws_sdk_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTransitGatewayConnectPeerAssociationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTransitGatewayConnectPeerAssociationsRequest:
    out: GetTransitGatewayConnectPeerAssociationsRequest = {}  # type: ignore[typeddict-item]
    return out
