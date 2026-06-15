"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetGatewayRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.gateway_identifier


class GetGatewayRequest(TypedDict):
    gateway_identifier: (
        "aws_sdk_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier"
    )
    """<p>The identifier of the gateway to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGatewayRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetGatewayRequest:
    out: GetGatewayRequest = {}  # type: ignore[typeddict-item]
    return out
