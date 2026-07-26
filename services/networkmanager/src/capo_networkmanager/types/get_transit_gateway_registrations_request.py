"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetTransitGatewayRegistrationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.global_network_id
    import capo_networkmanager.types.max_results
    import capo_networkmanager.types.next_token
    import capo_networkmanager.types.transit_gateway_arn_list


class GetTransitGatewayRegistrationsRequest(TypedDict, closed=True):
    global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network.</p>"""
    transit_gateway_arns: NotRequired[
        "capo_networkmanager.types.transit_gateway_arn_list.TransitGatewayArnList"
    ]
    """<p>The Amazon Resource Names (ARNs) of one or more transit gateways. The maximum is 10.</p>"""
    max_results: NotRequired["capo_networkmanager.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["capo_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTransitGatewayRegistrationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTransitGatewayRegistrationsRequest:
    out: GetTransitGatewayRegistrationsRequest = {}  # type: ignore[typeddict-item]
    return out
