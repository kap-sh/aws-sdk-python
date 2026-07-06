"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteGatewayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.gateway_identifier


class DeleteGatewayRequest(TypedDict, closed=True):
    gateway_identifier: (
        "aws_sdk_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier"
    )
    """<p>The identifier of the gateway to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteGatewayRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteGatewayRequest:
    out: DeleteGatewayRequest = {}  # type: ignore[typeddict-item]
    return out
