"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetNetworkTelemetryRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.aws_account_id
    import aws_sdk_networkmanager.types.constrained_string
    import aws_sdk_networkmanager.types.core_network_id
    import aws_sdk_networkmanager.types.external_region_code
    import aws_sdk_networkmanager.types.global_network_id
    import aws_sdk_networkmanager.types.max_results
    import aws_sdk_networkmanager.types.next_token
    import aws_sdk_networkmanager.types.resource_arn


class GetNetworkTelemetryRequest(TypedDict):
    global_network_id: "aws_sdk_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network.</p>"""
    core_network_id: NotRequired[
        "aws_sdk_networkmanager.types.core_network_id.CoreNetworkId"
    ]
    """<p>The ID of a core network.</p>"""
    registered_gateway_arn: NotRequired[
        "aws_sdk_networkmanager.types.resource_arn.ResourceArn"
    ]
    """<p>The ARN of the gateway.</p>"""
    aws_region: NotRequired[
        "aws_sdk_networkmanager.types.external_region_code.ExternalRegionCode"
    ]
    """<p>The Amazon Web Services Region.</p>"""
    account_id: NotRequired["aws_sdk_networkmanager.types.aws_account_id.AWSAccountId"]
    """<p>The Amazon Web Services account ID.</p>"""
    resource_type: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The resource type. The following are the supported resource types:</p> <ul> <li> <p> <code>connect-peer</code> </p> </li> <li> <p> <code>transit-gateway-connect-peer</code> </p> </li> <li> <p> <code>vpn-connection</code> </p> </li> </ul>"""
    resource_arn: NotRequired["aws_sdk_networkmanager.types.resource_arn.ResourceArn"]
    """<p>The ARN of the resource.</p>"""
    max_results: NotRequired["aws_sdk_networkmanager.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["aws_sdk_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNetworkTelemetryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetNetworkTelemetryRequest:
    out: GetNetworkTelemetryRequest = {}  # type: ignore[typeddict-item]
    return out
