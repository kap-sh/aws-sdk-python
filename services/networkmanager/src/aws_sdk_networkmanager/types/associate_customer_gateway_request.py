"""Generated from Smithy shape ``com.amazonaws.networkmanager#AssociateCustomerGatewayRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_networkmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.customer_gateway_arn
    import aws_sdk_networkmanager.types.device_id
    import aws_sdk_networkmanager.types.global_network_id
    import aws_sdk_networkmanager.types.link_id


class AssociateCustomerGatewayRequest(TypedDict):
    customer_gateway_arn: (
        "aws_sdk_networkmanager.types.customer_gateway_arn.CustomerGatewayArn"
    )
    """<p>The Amazon Resource Name (ARN) of the customer gateway.</p>"""
    global_network_id: "aws_sdk_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network.</p>"""
    device_id: "aws_sdk_networkmanager.types.device_id.DeviceId"
    """<p>The ID of the device.</p>"""
    link_id: NotRequired["aws_sdk_networkmanager.types.link_id.LinkId"]
    """<p>The ID of the link.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateCustomerGatewayRequest) -> dict:
    out: dict = {}
    out["CustomerGatewayArn"] = value["customer_gateway_arn"]
    out["DeviceId"] = value["device_id"]
    if "link_id" in value:
        out["LinkId"] = value["link_id"]
    return out


def deserialize_json(data: dict) -> AssociateCustomerGatewayRequest:
    out: AssociateCustomerGatewayRequest = {}  # type: ignore[typeddict-item]
    if "CustomerGatewayArn" in data:
        out["customer_gateway_arn"] = data["CustomerGatewayArn"]
    else:
        raise DeserializationError(
            "AssociateCustomerGatewayRequest.customer_gateway_arn required"
        )
    if "DeviceId" in data:
        out["device_id"] = data["DeviceId"]
    else:
        raise DeserializationError("AssociateCustomerGatewayRequest.device_id required")
    if "LinkId" in data:
        out["link_id"] = data["LinkId"]
    return out
