"""Generated from Smithy shape ``com.amazonaws.networkmanager#RegisterTransitGatewayRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_networkmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.global_network_id
    import aws_sdk_networkmanager.types.transit_gateway_arn


class RegisterTransitGatewayRequest(TypedDict):
    global_network_id: "aws_sdk_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network.</p>"""
    transit_gateway_arn: (
        "aws_sdk_networkmanager.types.transit_gateway_arn.TransitGatewayArn"
    )
    """<p>The Amazon Resource Name (ARN) of the transit gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterTransitGatewayRequest) -> dict:
    out: dict = {}
    out["TransitGatewayArn"] = value["transit_gateway_arn"]
    return out


def deserialize_json(data: dict) -> RegisterTransitGatewayRequest:
    out: RegisterTransitGatewayRequest = {}  # type: ignore[typeddict-item]
    if "TransitGatewayArn" in data:
        out["transit_gateway_arn"] = data["TransitGatewayArn"]
    else:
        raise DeserializationError(
            "RegisterTransitGatewayRequest.transit_gateway_arn required"
        )
    return out
