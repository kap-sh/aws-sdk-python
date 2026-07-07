"""Generated from Smithy shape ``com.amazonaws.mediaconnect#CreateGatewayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.__list_of_gateway_network
    import aws_sdk_mediaconnect.types.__list_of_string


class CreateGatewayRequest(TypedDict, closed=True):
    egress_cidr_blocks: NotRequired[
        "aws_sdk_mediaconnect.types.__list_of_string.__listOfString"
    ]
    """<p> The range of IP addresses that are allowed to contribute content or initiate output requests for flows communicating with this gateway. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.</p>"""
    name: NotRequired["str"]
    """<p> The name of the gateway. This name can not be modified after the gateway is created.</p>"""
    networks: NotRequired[
        "aws_sdk_mediaconnect.types.__list_of_gateway_network.__listOfGatewayNetwork"
    ]
    """<p> The list of networks that you want to add to the gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGatewayRequest) -> dict:
    out: dict = {}
    if "egress_cidr_blocks" in value:
        import aws_sdk_mediaconnect.types.__list_of_string

        out["egressCidrBlocks"] = (
            aws_sdk_mediaconnect.types.__list_of_string.serialize_json(
                value["egress_cidr_blocks"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "networks" in value:
        import aws_sdk_mediaconnect.types.__list_of_gateway_network

        out["networks"] = (
            aws_sdk_mediaconnect.types.__list_of_gateway_network.serialize_json(
                value["networks"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateGatewayRequest:
    out: CreateGatewayRequest = {}  # type: ignore[typeddict-item]
    if "egressCidrBlocks" in data:
        import aws_sdk_mediaconnect.types.__list_of_string

        out["egress_cidr_blocks"] = (
            aws_sdk_mediaconnect.types.__list_of_string.deserialize_json(
                data["egressCidrBlocks"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "networks" in data:
        import aws_sdk_mediaconnect.types.__list_of_gateway_network

        out["networks"] = (
            aws_sdk_mediaconnect.types.__list_of_gateway_network.deserialize_json(
                data["networks"]
            )
        )
    return out
