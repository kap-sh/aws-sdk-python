"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessAgentCoreGatewayConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.gateway_arn
    import aws_sdk_bedrock_agentcore.types.harness_gateway_outbound_auth


class HarnessAgentCoreGatewayConfig(TypedDict, closed=True):
    gateway_arn: "aws_sdk_bedrock_agentcore.types.gateway_arn.GatewayArn"
    """<p>The ARN of the desired AgentCore Gateway.</p>"""
    outbound_auth: NotRequired[
        "aws_sdk_bedrock_agentcore.types.harness_gateway_outbound_auth.HarnessGatewayOutboundAuth"
    ]
    """<p>How harness authenticates to this Gateway. Defaults to AWS_IAM (SigV4) if omitted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessAgentCoreGatewayConfig) -> dict:
    out: dict = {}
    out["gatewayArn"] = value["gateway_arn"]
    if "outbound_auth" in value:
        import aws_sdk_bedrock_agentcore.types.harness_gateway_outbound_auth

        out["outboundAuth"] = (
            aws_sdk_bedrock_agentcore.types.harness_gateway_outbound_auth.serialize_json(
                value["outbound_auth"]
            )
        )
    return out


def deserialize_json(data: dict) -> HarnessAgentCoreGatewayConfig:
    out: HarnessAgentCoreGatewayConfig = {}  # type: ignore[typeddict-item]
    if "gatewayArn" in data:
        out["gateway_arn"] = data["gatewayArn"]
    else:
        raise DeserializationError("HarnessAgentCoreGatewayConfig.gateway_arn required")
    if "outboundAuth" in data:
        import aws_sdk_bedrock_agentcore.types.harness_gateway_outbound_auth

        out["outbound_auth"] = (
            aws_sdk_bedrock_agentcore.types.harness_gateway_outbound_auth.deserialize_json(
                data["outboundAuth"]
            )
        )
    return out
