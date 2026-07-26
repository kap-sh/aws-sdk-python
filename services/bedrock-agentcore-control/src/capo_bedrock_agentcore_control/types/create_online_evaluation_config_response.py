"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateOnlineEvaluationConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore_control.types.online_evaluation_config_arn
    import capo_bedrock_agentcore_control.types.online_evaluation_config_id
    import capo_bedrock_agentcore_control.types.online_evaluation_config_status
    import capo_bedrock_agentcore_control.types.online_evaluation_execution_status
    import capo_bedrock_agentcore_control.types.output_config


class CreateOnlineEvaluationConfigResponse(TypedDict, closed=True):
    online_evaluation_config_arn: "capo_bedrock_agentcore_control.types.online_evaluation_config_arn.OnlineEvaluationConfigArn"
    """<p> The Amazon Resource Name (ARN) of the created online evaluation configuration. </p>"""
    online_evaluation_config_id: "capo_bedrock_agentcore_control.types.online_evaluation_config_id.OnlineEvaluationConfigId"
    """<p> The unique identifier of the created online evaluation configuration. </p>"""
    created_at: "datetime.datetime"
    """<p> The timestamp when the online evaluation configuration was created. </p>"""
    output_config: NotRequired[
        "capo_bedrock_agentcore_control.types.output_config.OutputConfig"
    ]
    status: "capo_bedrock_agentcore_control.types.online_evaluation_config_status.OnlineEvaluationConfigStatus"
    """<p> The status of the online evaluation configuration. </p>"""
    execution_status: "capo_bedrock_agentcore_control.types.online_evaluation_execution_status.OnlineEvaluationExecutionStatus"
    """<p> The execution status indicating whether the online evaluation is currently running. </p>"""
    failure_reason: NotRequired["str"]
    """<p> The reason for failure if the online evaluation configuration creation or execution failed. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateOnlineEvaluationConfigResponse) -> dict:
    out: dict = {}
    out["onlineEvaluationConfigArn"] = value["online_evaluation_config_arn"]
    out["onlineEvaluationConfigId"] = value["online_evaluation_config_id"]
    import capo_bedrock_agentcore_control.types._prelude.timestamp

    out["createdAt"] = (
        capo_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    )
    if "output_config" in value:
        import capo_bedrock_agentcore_control.types.output_config

        out["outputConfig"] = (
            capo_bedrock_agentcore_control.types.output_config.serialize_json(
                value["output_config"]
            )
        )
    import capo_bedrock_agentcore_control.types.online_evaluation_config_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.online_evaluation_config_status.serialize_json(
            value["status"]
        )
    )
    import capo_bedrock_agentcore_control.types.online_evaluation_execution_status

    out["executionStatus"] = (
        capo_bedrock_agentcore_control.types.online_evaluation_execution_status.serialize_json(
            value["execution_status"]
        )
    )
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    return out


def deserialize_json(data: dict) -> CreateOnlineEvaluationConfigResponse:
    out: CreateOnlineEvaluationConfigResponse = {}  # type: ignore[typeddict-item]
    if "onlineEvaluationConfigArn" in data:
        out["online_evaluation_config_arn"] = data["onlineEvaluationConfigArn"]
    else:
        raise DeserializationError(
            "CreateOnlineEvaluationConfigResponse.online_evaluation_config_arn required"
        )
    if "onlineEvaluationConfigId" in data:
        out["online_evaluation_config_id"] = data["onlineEvaluationConfigId"]
    else:
        raise DeserializationError(
            "CreateOnlineEvaluationConfigResponse.online_evaluation_config_id required"
        )
    if "createdAt" in data:
        import capo_bedrock_agentcore_control.types._prelude.timestamp

        out["created_at"] = (
            capo_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError(
            "CreateOnlineEvaluationConfigResponse.created_at required"
        )
    if "outputConfig" in data:
        import capo_bedrock_agentcore_control.types.output_config

        out["output_config"] = (
            capo_bedrock_agentcore_control.types.output_config.deserialize_json(
                data["outputConfig"]
            )
        )
    if "status" in data:
        import capo_bedrock_agentcore_control.types.online_evaluation_config_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.online_evaluation_config_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError(
            "CreateOnlineEvaluationConfigResponse.status required"
        )
    if "executionStatus" in data:
        import capo_bedrock_agentcore_control.types.online_evaluation_execution_status

        out["execution_status"] = (
            capo_bedrock_agentcore_control.types.online_evaluation_execution_status.deserialize_json(
                data["executionStatus"]
            )
        )
    else:
        raise DeserializationError(
            "CreateOnlineEvaluationConfigResponse.execution_status required"
        )
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    return out
