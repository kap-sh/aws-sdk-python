"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetNetworkResourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.aws_account_id
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.core_network_id
    import capo_networkmanager.types.external_region_code
    import capo_networkmanager.types.global_network_id
    import capo_networkmanager.types.max_results
    import capo_networkmanager.types.next_token
    import capo_networkmanager.types.resource_arn


class GetNetworkResourcesRequest(TypedDict, closed=True):
    global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network.</p>"""
    core_network_id: NotRequired[
        "capo_networkmanager.types.core_network_id.CoreNetworkId"
    ]
    """<p>The ID of a core network.</p>"""
    registered_gateway_arn: NotRequired[
        "capo_networkmanager.types.resource_arn.ResourceArn"
    ]
    """<p>The ARN of the gateway.</p>"""
    aws_region: NotRequired[
        "capo_networkmanager.types.external_region_code.ExternalRegionCode"
    ]
    """<p>The Amazon Web Services Region.</p>"""
    account_id: NotRequired["capo_networkmanager.types.aws_account_id.AWSAccountId"]
    """<p>The Amazon Web Services account ID.</p>"""
    resource_type: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The resource type.</p> <p>The following are the supported resource types for Direct Connect:</p> <ul> <li> <p> <code>dxcon</code> </p> </li> <li> <p> <code>dx-gateway</code> </p> </li> <li> <p> <code>dx-vif</code> </p> </li> </ul> <p>The following are the supported resource types for Network Manager:</p> <ul> <li> <p> <code>attachment</code> </p> </li> <li> <p> <code>connect-peer</code> </p> </li> <li> <p> <code>connection</code> </p> </li> <li> <p> <code>core-network</code> </p> </li> <li> <p> <code>device</code> </p> </li> <li> <p> <code>link</code> </p> </li> <li> <p> <code>peering</code> </p> </li> <li> <p> <code>site</code> </p> </li> </ul> <p>The following are the supported resource types for Amazon VPC:</p> <ul> <li> <p> <code>customer-gateway</code> </p> </li> <li> <p> <code>transit-gateway</code> </p> </li> <li> <p> <code>transit-gateway-attachment</code> </p> </li> <li> <p> <code>transit-gateway-connect-peer</code> </p> </li> <li> <p> <code>transit-gateway-route-table</code> </p> </li> <li> <p> <code>vpn-connection</code> </p> </li> </ul>"""
    resource_arn: NotRequired["capo_networkmanager.types.resource_arn.ResourceArn"]
    """<p>The ARN of the resource.</p>"""
    max_results: NotRequired["capo_networkmanager.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["capo_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNetworkResourcesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetNetworkResourcesRequest:
    out: GetNetworkResourcesRequest = {}  # type: ignore[typeddict-item]
    return out
