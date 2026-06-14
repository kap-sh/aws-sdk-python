"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdateOnlineEvaluationConfigResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_arn
    import aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_id
    import aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_status
    import aws_sdk_bedrock_agentcore_control.types.online_evaluation_execution_status


class UpdateOnlineEvaluationConfigResponse(TypedDict):
    online_evaluation_config_arn: "aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_arn.OnlineEvaluationConfigArn"
    """<p> The Amazon Resource Name (ARN) of the updated online evaluation configuration. </p>"""
    online_evaluation_config_id: "aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_id.OnlineEvaluationConfigId"
    """<p> The unique identifier of the updated online evaluation configuration. </p>"""
    updated_at: "datetime.datetime"
    """<p> The timestamp when the online evaluation configuration was last updated. </p>"""
    status: "aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_status.OnlineEvaluationConfigStatus"
    """<p> The status of the online evaluation configuration. </p>"""
    execution_status: "aws_sdk_bedrock_agentcore_control.types.online_evaluation_execution_status.OnlineEvaluationExecutionStatus"
    """<p> The execution status indicating whether the online evaluation is currently running. </p>"""
    failure_reason: NotRequired["str"]
    """<p> The reason for failure if the online evaluation configuration update or execution failed. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateOnlineEvaluationConfigResponse) -> dict:
    out: dict = {}
    out["onlineEvaluationConfigArn"] = value["online_evaluation_config_arn"]
    out["onlineEvaluationConfigId"] = value["online_evaluation_config_id"]
    import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp

    out["updatedAt"] = (
        aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_status

    out["status"] = (
        aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_status.serialize_json(
            value["status"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types.online_evaluation_execution_status

    out["executionStatus"] = (
        aws_sdk_bedrock_agentcore_control.types.online_evaluation_execution_status.serialize_json(
            value["execution_status"]
        )
    )
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    return out


def deserialize_json(data: dict) -> UpdateOnlineEvaluationConfigResponse:
    out: UpdateOnlineEvaluationConfigResponse = {}  # type: ignore[typeddict-item]
    if "onlineEvaluationConfigArn" in data:
        out["online_evaluation_config_arn"] = data["onlineEvaluationConfigArn"]
    else:
        raise DeserializationError(
            "UpdateOnlineEvaluationConfigResponse.online_evaluation_config_arn required"
        )
    if "onlineEvaluationConfigId" in data:
        out["online_evaluation_config_id"] = data["onlineEvaluationConfigId"]
    else:
        raise DeserializationError(
            "UpdateOnlineEvaluationConfigResponse.online_evaluation_config_id required"
        )
    if "updatedAt" in data:
        import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateOnlineEvaluationConfigResponse.updated_at required"
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
            "UpdateOnlineEvaluationConfigResponse.status required"
        )
    if "executionStatus" in data:
        import aws_sdk_bedrock_agentcore_control.types.online_evaluation_execution_status

        out["execution_status"] = (
            aws_sdk_bedrock_agentcore_control.types.online_evaluation_execution_status.deserialize_json(
                data["executionStatus"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateOnlineEvaluationConfigResponse.execution_status required"
        )
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    return out
