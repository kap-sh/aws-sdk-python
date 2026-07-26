"""Generated from Smithy shape ``com.amazonaws.mediaconnect#Gateway``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.__list_of_gateway_network
    import capo_mediaconnect.types.__list_of_message_detail
    import capo_mediaconnect.types.__list_of_string
    import capo_mediaconnect.types.gateway_state


class Gateway(TypedDict, closed=True):
    egress_cidr_blocks: NotRequired[
        "capo_mediaconnect.types.__list_of_string.__listOfString"
    ]
    """<p> The range of IP addresses that contribute content or initiate output requests for flows communicating with this gateway. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.</p>"""
    gateway_arn: NotRequired["str"]
    """<p> The Amazon Resource Name (ARN) of the gateway.</p>"""
    gateway_messages: NotRequired[
        "capo_mediaconnect.types.__list_of_message_detail.__listOfMessageDetail"
    ]
    """<p>Messages with information about the gateway. </p>"""
    gateway_state: NotRequired["capo_mediaconnect.types.gateway_state.GatewayState"]
    """<p> The current status of the gateway.</p>"""
    name: NotRequired["str"]
    """<p> The name of the gateway. This name can not be modified after the gateway is created.</p>"""
    networks: NotRequired[
        "capo_mediaconnect.types.__list_of_gateway_network.__listOfGatewayNetwork"
    ]
    """<p> The list of networks in the gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Gateway) -> dict:
    out: dict = {}
    if "egress_cidr_blocks" in value:
        import capo_mediaconnect.types.__list_of_string

        out["egressCidrBlocks"] = (
            capo_mediaconnect.types.__list_of_string.serialize_json(
                value["egress_cidr_blocks"]
            )
        )
    if "gateway_arn" in value:
        out["gatewayArn"] = value["gateway_arn"]
    if "gateway_messages" in value:
        import capo_mediaconnect.types.__list_of_message_detail

        out["gatewayMessages"] = (
            capo_mediaconnect.types.__list_of_message_detail.serialize_json(
                value["gateway_messages"]
            )
        )
    if "gateway_state" in value:
        import capo_mediaconnect.types.gateway_state

        out["gatewayState"] = capo_mediaconnect.types.gateway_state.serialize_json(
            value["gateway_state"]
        )
    if "name" in value:
        out["name"] = value["name"]
    if "networks" in value:
        import capo_mediaconnect.types.__list_of_gateway_network

        out["networks"] = (
            capo_mediaconnect.types.__list_of_gateway_network.serialize_json(
                value["networks"]
            )
        )
    return out


def deserialize_json(data: dict) -> Gateway:
    out: Gateway = {}  # type: ignore[typeddict-item]
    if "egressCidrBlocks" in data:
        import capo_mediaconnect.types.__list_of_string

        out["egress_cidr_blocks"] = (
            capo_mediaconnect.types.__list_of_string.deserialize_json(
                data["egressCidrBlocks"]
            )
        )
    if "gatewayArn" in data:
        out["gateway_arn"] = data["gatewayArn"]
    if "gatewayMessages" in data:
        import capo_mediaconnect.types.__list_of_message_detail

        out["gateway_messages"] = (
            capo_mediaconnect.types.__list_of_message_detail.deserialize_json(
                data["gatewayMessages"]
            )
        )
    if "gatewayState" in data:
        import capo_mediaconnect.types.gateway_state

        out["gateway_state"] = capo_mediaconnect.types.gateway_state.deserialize_json(
            data["gatewayState"]
        )
    if "name" in data:
        out["name"] = data["name"]
    if "networks" in data:
        import capo_mediaconnect.types.__list_of_gateway_network

        out["networks"] = (
            capo_mediaconnect.types.__list_of_gateway_network.deserialize_json(
                data["networks"]
            )
        )
    return out
