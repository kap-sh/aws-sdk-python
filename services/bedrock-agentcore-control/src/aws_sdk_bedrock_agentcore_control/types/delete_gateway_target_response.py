"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteGatewayTargetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.gateway_arn
    import aws_sdk_bedrock_agentcore_control.types.status_reasons
    import aws_sdk_bedrock_agentcore_control.types.target_id
    import aws_sdk_bedrock_agentcore_control.types.target_status


class DeleteGatewayTargetResponse(TypedDict, closed=True):
    gateway_arn: "aws_sdk_bedrock_agentcore_control.types.gateway_arn.GatewayArn"
    """<p>The Amazon Resource Name (ARN) of the gateway.</p>"""
    target_id: "aws_sdk_bedrock_agentcore_control.types.target_id.TargetId"
    """<p>The unique identifier of the deleted gateway target.</p>"""
    status: "aws_sdk_bedrock_agentcore_control.types.target_status.TargetStatus"
    """<p>The current status of the gateway target deletion.</p>"""
    status_reasons: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.status_reasons.StatusReasons"
    ]
    """<p>The reasons for the current status of the gateway target deletion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteGatewayTargetResponse) -> dict:
    out: dict = {}
    out["gatewayArn"] = value["gateway_arn"]
    out["targetId"] = value["target_id"]
    import aws_sdk_bedrock_agentcore_control.types.target_status

    out["status"] = (
        aws_sdk_bedrock_agentcore_control.types.target_status.serialize_json(
            value["status"]
        )
    )
    if "status_reasons" in value:
        import aws_sdk_bedrock_agentcore_control.types.status_reasons

        out["statusReasons"] = (
            aws_sdk_bedrock_agentcore_control.types.status_reasons.serialize_json(
                value["status_reasons"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteGatewayTargetResponse:
    out: DeleteGatewayTargetResponse = {}  # type: ignore[typeddict-item]
    if "gatewayArn" in data:
        out["gateway_arn"] = data["gatewayArn"]
    else:
        raise DeserializationError("DeleteGatewayTargetResponse.gateway_arn required")
    if "targetId" in data:
        out["target_id"] = data["targetId"]
    else:
        raise DeserializationError("DeleteGatewayTargetResponse.target_id required")
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.target_status

        out["status"] = (
            aws_sdk_bedrock_agentcore_control.types.target_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("DeleteGatewayTargetResponse.status required")
    if "statusReasons" in data:
        import aws_sdk_bedrock_agentcore_control.types.status_reasons

        out["status_reasons"] = (
            aws_sdk_bedrock_agentcore_control.types.status_reasons.deserialize_json(
                data["statusReasons"]
            )
        )
    return out
