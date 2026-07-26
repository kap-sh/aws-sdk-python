"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#OnlineEvaluationConfigSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore_control.types.evaluation_config_description
    import capo_bedrock_agentcore_control.types.evaluation_config_name
    import capo_bedrock_agentcore_control.types.online_evaluation_config_arn
    import capo_bedrock_agentcore_control.types.online_evaluation_config_id
    import capo_bedrock_agentcore_control.types.online_evaluation_config_status
    import capo_bedrock_agentcore_control.types.online_evaluation_execution_status


class OnlineEvaluationConfigSummary(TypedDict, closed=True):
    online_evaluation_config_arn: "capo_bedrock_agentcore_control.types.online_evaluation_config_arn.OnlineEvaluationConfigArn"
    """<p> The Amazon Resource Name (ARN) of the online evaluation configuration. </p>"""
    online_evaluation_config_id: "capo_bedrock_agentcore_control.types.online_evaluation_config_id.OnlineEvaluationConfigId"
    """<p> The unique identifier of the online evaluation configuration. </p>"""
    online_evaluation_config_name: "capo_bedrock_agentcore_control.types.evaluation_config_name.EvaluationConfigName"
    """<p> The name of the online evaluation configuration. </p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.evaluation_config_description.EvaluationConfigDescription"
    ]
    """<p> The description of the online evaluation configuration. </p>"""
    status: "capo_bedrock_agentcore_control.types.online_evaluation_config_status.OnlineEvaluationConfigStatus"
    """<p> The status of the online evaluation configuration. </p>"""
    execution_status: "capo_bedrock_agentcore_control.types.online_evaluation_execution_status.OnlineEvaluationExecutionStatus"
    """<p> The execution status indicating whether the online evaluation is currently running. </p>"""
    created_at: "datetime.datetime"
    """<p> The timestamp when the online evaluation configuration was created. </p>"""
    updated_at: "datetime.datetime"
    """<p> The timestamp when the online evaluation configuration was last updated. </p>"""
    failure_reason: NotRequired["str"]
    """<p> The reason for failure if the online evaluation configuration execution failed. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OnlineEvaluationConfigSummary) -> dict:
    out: dict = {}
    out["onlineEvaluationConfigArn"] = value["online_evaluation_config_arn"]
    out["onlineEvaluationConfigId"] = value["online_evaluation_config_id"]
    out["onlineEvaluationConfigName"] = value["online_evaluation_config_name"]
    if "description" in value:
        out["description"] = value["description"]
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
    import capo_bedrock_agentcore_control.types._prelude.timestamp

    out["createdAt"] = (
        capo_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    )
    import capo_bedrock_agentcore_control.types._prelude.timestamp

    out["updatedAt"] = (
        capo_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    )
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    return out


def deserialize_json(data: dict) -> OnlineEvaluationConfigSummary:
    out: OnlineEvaluationConfigSummary = {}  # type: ignore[typeddict-item]
    if "onlineEvaluationConfigArn" in data:
        out["online_evaluation_config_arn"] = data["onlineEvaluationConfigArn"]
    else:
        raise DeserializationError(
            "OnlineEvaluationConfigSummary.online_evaluation_config_arn required"
        )
    if "onlineEvaluationConfigId" in data:
        out["online_evaluation_config_id"] = data["onlineEvaluationConfigId"]
    else:
        raise DeserializationError(
            "OnlineEvaluationConfigSummary.online_evaluation_config_id required"
        )
    if "onlineEvaluationConfigName" in data:
        out["online_evaluation_config_name"] = data["onlineEvaluationConfigName"]
    else:
        raise DeserializationError(
            "OnlineEvaluationConfigSummary.online_evaluation_config_name required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "status" in data:
        import capo_bedrock_agentcore_control.types.online_evaluation_config_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.online_evaluation_config_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("OnlineEvaluationConfigSummary.status required")
    if "executionStatus" in data:
        import capo_bedrock_agentcore_control.types.online_evaluation_execution_status

        out["execution_status"] = (
            capo_bedrock_agentcore_control.types.online_evaluation_execution_status.deserialize_json(
                data["executionStatus"]
            )
        )
    else:
        raise DeserializationError(
            "OnlineEvaluationConfigSummary.execution_status required"
        )
    if "createdAt" in data:
        import capo_bedrock_agentcore_control.types._prelude.timestamp

        out["created_at"] = (
            capo_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("OnlineEvaluationConfigSummary.created_at required")
    if "updatedAt" in data:
        import capo_bedrock_agentcore_control.types._prelude.timestamp

        out["updated_at"] = (
            capo_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("OnlineEvaluationConfigSummary.updated_at required")
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    return out
