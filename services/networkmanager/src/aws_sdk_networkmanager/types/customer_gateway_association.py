"""Generated from Smithy shape ``com.amazonaws.networkmanager#CustomerGatewayAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.customer_gateway_arn
    import aws_sdk_networkmanager.types.customer_gateway_association_state
    import aws_sdk_networkmanager.types.device_id
    import aws_sdk_networkmanager.types.global_network_id
    import aws_sdk_networkmanager.types.link_id


class CustomerGatewayAssociation(TypedDict, closed=True):
    customer_gateway_arn: NotRequired[
        "aws_sdk_networkmanager.types.customer_gateway_arn.CustomerGatewayArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the customer gateway.</p>"""
    global_network_id: NotRequired[
        "aws_sdk_networkmanager.types.global_network_id.GlobalNetworkId"
    ]
    """<p>The ID of the global network.</p>"""
    device_id: NotRequired["aws_sdk_networkmanager.types.device_id.DeviceId"]
    """<p>The ID of the device.</p>"""
    link_id: NotRequired["aws_sdk_networkmanager.types.link_id.LinkId"]
    """<p>The ID of the link.</p>"""
    state: NotRequired[
        "aws_sdk_networkmanager.types.customer_gateway_association_state.CustomerGatewayAssociationState"
    ]
    """<p>The association state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomerGatewayAssociation) -> dict:
    out: dict = {}
    if "customer_gateway_arn" in value:
        out["CustomerGatewayArn"] = value["customer_gateway_arn"]
    if "global_network_id" in value:
        out["GlobalNetworkId"] = value["global_network_id"]
    if "device_id" in value:
        out["DeviceId"] = value["device_id"]
    if "link_id" in value:
        out["LinkId"] = value["link_id"]
    if "state" in value:
        import aws_sdk_networkmanager.types.customer_gateway_association_state

        out["State"] = (
            aws_sdk_networkmanager.types.customer_gateway_association_state.serialize_json(
                value["state"]
            )
        )
    return out


def deserialize_json(data: dict) -> CustomerGatewayAssociation:
    out: CustomerGatewayAssociation = {}  # type: ignore[typeddict-item]
    if "CustomerGatewayArn" in data:
        out["customer_gateway_arn"] = data["CustomerGatewayArn"]
    if "GlobalNetworkId" in data:
        out["global_network_id"] = data["GlobalNetworkId"]
    if "DeviceId" in data:
        out["device_id"] = data["DeviceId"]
    if "LinkId" in data:
        out["link_id"] = data["LinkId"]
    if "State" in data:
        import aws_sdk_networkmanager.types.customer_gateway_association_state

        out["state"] = (
            aws_sdk_networkmanager.types.customer_gateway_association_state.deserialize_json(
                data["State"]
            )
        )
    return out
