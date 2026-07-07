"""Generated from Smithy shape ``com.amazonaws.rtbfabric#UpdateRequesterGatewayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rtbfabric.types.gateway_id


class UpdateRequesterGatewayRequest(TypedDict, closed=True):
    client_token: "str"
    """<p>The unique client token.</p>"""
    gateway_id: "aws_sdk_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""
    description: NotRequired["str"]
    """<p>An optional description for the requester gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRequesterGatewayRequest) -> dict:
    out: dict = {}
    out["clientToken"] = value["client_token"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateRequesterGatewayRequest:
    out: UpdateRequesterGatewayRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError(
            "UpdateRequesterGatewayRequest.client_token required"
        )
    if "description" in data:
        out["description"] = data["description"]
    return out
