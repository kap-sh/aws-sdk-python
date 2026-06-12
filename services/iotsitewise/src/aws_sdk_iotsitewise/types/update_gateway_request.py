"""Generated from Smithy shape ``com.amazonaws.iotsitewise#UpdateGatewayRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.gateway_name
    import aws_sdk_iotsitewise.types.id


class UpdateGatewayRequest(TypedDict):
    gateway_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the gateway to update.</p>"""
    gateway_name: "aws_sdk_iotsitewise.types.gateway_name.GatewayName"
    """<p>A unique name for the gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGatewayRequest) -> dict:
    out: dict = {}
    out["gatewayName"] = value["gateway_name"]
    return out


def deserialize_json(data: dict) -> UpdateGatewayRequest:
    out: UpdateGatewayRequest = {}  # type: ignore[typeddict-item]
    if "gatewayName" in data:
        out["gateway_name"] = data["gatewayName"]
    else:
        raise DeserializationError("UpdateGatewayRequest.gateway_name required")
    return out
