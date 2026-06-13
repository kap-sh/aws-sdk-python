"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteGatewayResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.gateway_id
    import aws_sdk_bedrock_agentcore_control.types.gateway_status
    import aws_sdk_bedrock_agentcore_control.types.status_reasons

class DeleteGatewayResponse(TypedDict):
    gateway_id: "aws_sdk_bedrock_agentcore_control.types.gateway_id.GatewayId"
    """<p>The unique identifier of the deleted gateway.</p>"""
    status: "aws_sdk_bedrock_agentcore_control.types.gateway_status.GatewayStatus"
    """<p>The current status of the gateway deletion.</p>"""
    status_reasons: NotRequired["aws_sdk_bedrock_agentcore_control.types.status_reasons.StatusReasons"]
    """<p>The reasons for the current status of the gateway deletion.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DeleteGatewayResponse) -> dict:
    out: dict = {}
    out["gatewayId"] = value["gateway_id"]
    import aws_sdk_bedrock_agentcore_control.types.gateway_status
    out["status"] = aws_sdk_bedrock_agentcore_control.types.gateway_status.serialize_json(value["status"])
    if "status_reasons" in value:
        import aws_sdk_bedrock_agentcore_control.types.status_reasons
        out["statusReasons"] = aws_sdk_bedrock_agentcore_control.types.status_reasons.serialize_json(value["status_reasons"])
    return out


def deserialize_json(data: dict) -> DeleteGatewayResponse:
    out: DeleteGatewayResponse = {}  # type: ignore[typeddict-item]
    if "gatewayId" in data:
        out["gateway_id"] = data["gatewayId"]
    else:
        raise DeserializationError("DeleteGatewayResponse.gateway_id required")
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.gateway_status
        out["status"] = aws_sdk_bedrock_agentcore_control.types.gateway_status.deserialize_json(data["status"])
    else:
        raise DeserializationError("DeleteGatewayResponse.status required")
    if "statusReasons" in data:
        import aws_sdk_bedrock_agentcore_control.types.status_reasons
        out["status_reasons"] = aws_sdk_bedrock_agentcore_control.types.status_reasons.deserialize_json(data["statusReasons"])
    return out