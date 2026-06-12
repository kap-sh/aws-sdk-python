"""Generated from Smithy shape ``com.amazonaws.networkmanager#DisassociateCustomerGatewayRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.customer_gateway_arn
    import aws_sdk_networkmanager.types.global_network_id


class DisassociateCustomerGatewayRequest(TypedDict):
    global_network_id: "aws_sdk_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network.</p>"""
    customer_gateway_arn: (
        "aws_sdk_networkmanager.types.customer_gateway_arn.CustomerGatewayArn"
    )
    """<p>The Amazon Resource Name (ARN) of the customer gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateCustomerGatewayRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateCustomerGatewayRequest:
    out: DisassociateCustomerGatewayRequest = {}  # type: ignore[typeddict-item]
    return out
