"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetCustomerGatewayAssociationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.customer_gateway_arn_list
    import aws_sdk_networkmanager.types.global_network_id
    import aws_sdk_networkmanager.types.max_results
    import aws_sdk_networkmanager.types.next_token


class GetCustomerGatewayAssociationsRequest(TypedDict):
    global_network_id: "aws_sdk_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network.</p>"""
    customer_gateway_arns: NotRequired[
        "aws_sdk_networkmanager.types.customer_gateway_arn_list.CustomerGatewayArnList"
    ]
    """<p>One or more customer gateway Amazon Resource Names (ARNs). The maximum is 10.</p>"""
    max_results: NotRequired["aws_sdk_networkmanager.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["aws_sdk_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCustomerGatewayAssociationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCustomerGatewayAssociationsRequest:
    out: GetCustomerGatewayAssociationsRequest = {}  # type: ignore[typeddict-item]
    return out
