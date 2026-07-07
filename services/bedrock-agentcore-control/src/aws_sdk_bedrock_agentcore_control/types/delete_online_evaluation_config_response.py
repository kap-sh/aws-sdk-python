"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteOnlineEvaluationConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_arn
    import aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_id
    import aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_status


class DeleteOnlineEvaluationConfigResponse(TypedDict, closed=True):
    online_evaluation_config_arn: "aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_arn.OnlineEvaluationConfigArn"
    """<p> The Amazon Resource Name (ARN) of the deleted online evaluation configuration. </p>"""
    online_evaluation_config_id: "aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_id.OnlineEvaluationConfigId"
    """<p> The unique identifier of the deleted online evaluation configuration. </p>"""
    status: "aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_status.OnlineEvaluationConfigStatus"
    """<p> The status of the online evaluation configuration deletion operation. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteOnlineEvaluationConfigResponse) -> dict:
    out: dict = {}
    out["onlineEvaluationConfigArn"] = value["online_evaluation_config_arn"]
    out["onlineEvaluationConfigId"] = value["online_evaluation_config_id"]
    import aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_status

    out["status"] = (
        aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeleteOnlineEvaluationConfigResponse:
    out: DeleteOnlineEvaluationConfigResponse = {}  # type: ignore[typeddict-item]
    if "onlineEvaluationConfigArn" in data:
        out["online_evaluation_config_arn"] = data["onlineEvaluationConfigArn"]
    else:
        raise DeserializationError(
            "DeleteOnlineEvaluationConfigResponse.online_evaluation_config_arn required"
        )
    if "onlineEvaluationConfigId" in data:
        out["online_evaluation_config_id"] = data["onlineEvaluationConfigId"]
    else:
        raise DeserializationError(
            "DeleteOnlineEvaluationConfigResponse.online_evaluation_config_id required"
        )
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_status

        out["status"] = (
            aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteOnlineEvaluationConfigResponse.status required"
        )
    return out
