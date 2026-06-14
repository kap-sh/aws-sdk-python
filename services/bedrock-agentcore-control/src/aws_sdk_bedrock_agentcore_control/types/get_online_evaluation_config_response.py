"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetOnlineEvaluationConfigResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_bedrock_agentcore_control.types.data_source_config
    import aws_sdk_bedrock_agentcore_control.types.evaluation_config_description
    import aws_sdk_bedrock_agentcore_control.types.evaluation_config_name
    import aws_sdk_bedrock_agentcore_control.types.evaluator_list
    import aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_arn
    import aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_id
    import aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_status
    import aws_sdk_bedrock_agentcore_control.types.online_evaluation_execution_status
    import aws_sdk_bedrock_agentcore_control.types.output_config
    import aws_sdk_bedrock_agentcore_control.types.role_arn
    import aws_sdk_bedrock_agentcore_control.types.rule


class GetOnlineEvaluationConfigResponse(TypedDict):
    online_evaluation_config_arn: "aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_arn.OnlineEvaluationConfigArn"
    """<p> The Amazon Resource Name (ARN) of the online evaluation configuration. </p>"""
    online_evaluation_config_id: "aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_id.OnlineEvaluationConfigId"
    """<p> The unique identifier of the online evaluation configuration. </p>"""
    online_evaluation_config_name: "aws_sdk_bedrock_agentcore_control.types.evaluation_config_name.EvaluationConfigName"
    """<p> The name of the online evaluation configuration. </p>"""
    description: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.evaluation_config_description.EvaluationConfigDescription"
    ]
    """<p> The description of the online evaluation configuration. </p>"""
    rule: "aws_sdk_bedrock_agentcore_control.types.rule.Rule"
    """<p> The evaluation rule containing sampling configuration, filters, and session settings. </p>"""
    data_source_config: (
        "aws_sdk_bedrock_agentcore_control.types.data_source_config.DataSourceConfig"
    )
    """<p> The data source configuration specifying CloudWatch log groups and service names to monitor. </p>"""
    evaluators: "aws_sdk_bedrock_agentcore_control.types.evaluator_list.EvaluatorList"
    """<p> The list of evaluators applied during online evaluation. </p>"""
    output_config: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.output_config.OutputConfig"
    ]
    """<p> The output configuration specifying where evaluation results are written. </p>"""
    evaluation_execution_role_arn: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.role_arn.RoleArn"
    ]
    """<p> The Amazon Resource Name (ARN) of the IAM role used for evaluation execution. </p>"""
    status: "aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_status.OnlineEvaluationConfigStatus"
    """<p> The status of the online evaluation configuration. </p>"""
    execution_status: "aws_sdk_bedrock_agentcore_control.types.online_evaluation_execution_status.OnlineEvaluationExecutionStatus"
    """<p> The execution status indicating whether the online evaluation is currently running. </p>"""
    created_at: "datetime.datetime"
    """<p> The timestamp when the online evaluation configuration was created. </p>"""
    updated_at: "datetime.datetime"
    """<p> The timestamp when the online evaluation configuration was last updated. </p>"""
    failure_reason: NotRequired["str"]
    """<p> The reason for failure if the online evaluation configuration execution failed. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOnlineEvaluationConfigResponse) -> dict:
    out: dict = {}
    out["onlineEvaluationConfigArn"] = value["online_evaluation_config_arn"]
    out["onlineEvaluationConfigId"] = value["online_evaluation_config_id"]
    out["onlineEvaluationConfigName"] = value["online_evaluation_config_name"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_bedrock_agentcore_control.types.rule

    out["rule"] = aws_sdk_bedrock_agentcore_control.types.rule.serialize_json(
        value["rule"]
    )
    import aws_sdk_bedrock_agentcore_control.types.data_source_config

    out["dataSourceConfig"] = (
        aws_sdk_bedrock_agentcore_control.types.data_source_config.serialize_json(
            value["data_source_config"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types.evaluator_list

    out["evaluators"] = (
        aws_sdk_bedrock_agentcore_control.types.evaluator_list.serialize_json(
            value["evaluators"]
        )
    )
    if "output_config" in value:
        import aws_sdk_bedrock_agentcore_control.types.output_config

        out["outputConfig"] = (
            aws_sdk_bedrock_agentcore_control.types.output_config.serialize_json(
                value["output_config"]
            )
        )
    if "evaluation_execution_role_arn" in value:
        out["evaluationExecutionRoleArn"] = value["evaluation_execution_role_arn"]
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
    import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp

    out["createdAt"] = (
        aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp

    out["updatedAt"] = (
        aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    )
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    return out


def deserialize_json(data: dict) -> GetOnlineEvaluationConfigResponse:
    out: GetOnlineEvaluationConfigResponse = {}  # type: ignore[typeddict-item]
    if "onlineEvaluationConfigArn" in data:
        out["online_evaluation_config_arn"] = data["onlineEvaluationConfigArn"]
    else:
        raise DeserializationError(
            "GetOnlineEvaluationConfigResponse.online_evaluation_config_arn required"
        )
    if "onlineEvaluationConfigId" in data:
        out["online_evaluation_config_id"] = data["onlineEvaluationConfigId"]
    else:
        raise DeserializationError(
            "GetOnlineEvaluationConfigResponse.online_evaluation_config_id required"
        )
    if "onlineEvaluationConfigName" in data:
        out["online_evaluation_config_name"] = data["onlineEvaluationConfigName"]
    else:
        raise DeserializationError(
            "GetOnlineEvaluationConfigResponse.online_evaluation_config_name required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "rule" in data:
        import aws_sdk_bedrock_agentcore_control.types.rule

        out["rule"] = aws_sdk_bedrock_agentcore_control.types.rule.deserialize_json(
            data["rule"]
        )
    else:
        raise DeserializationError("GetOnlineEvaluationConfigResponse.rule required")
    if "dataSourceConfig" in data:
        import aws_sdk_bedrock_agentcore_control.types.data_source_config

        out["data_source_config"] = (
            aws_sdk_bedrock_agentcore_control.types.data_source_config.deserialize_json(
                data["dataSourceConfig"]
            )
        )
    else:
        raise DeserializationError(
            "GetOnlineEvaluationConfigResponse.data_source_config required"
        )
    if "evaluators" in data:
        import aws_sdk_bedrock_agentcore_control.types.evaluator_list

        out["evaluators"] = (
            aws_sdk_bedrock_agentcore_control.types.evaluator_list.deserialize_json(
                data["evaluators"]
            )
        )
    else:
        raise DeserializationError(
            "GetOnlineEvaluationConfigResponse.evaluators required"
        )
    if "outputConfig" in data:
        import aws_sdk_bedrock_agentcore_control.types.output_config

        out["output_config"] = (
            aws_sdk_bedrock_agentcore_control.types.output_config.deserialize_json(
                data["outputConfig"]
            )
        )
    if "evaluationExecutionRoleArn" in data:
        out["evaluation_execution_role_arn"] = data["evaluationExecutionRoleArn"]
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_status

        out["status"] = (
            aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("GetOnlineEvaluationConfigResponse.status required")
    if "executionStatus" in data:
        import aws_sdk_bedrock_agentcore_control.types.online_evaluation_execution_status

        out["execution_status"] = (
            aws_sdk_bedrock_agentcore_control.types.online_evaluation_execution_status.deserialize_json(
                data["executionStatus"]
            )
        )
    else:
        raise DeserializationError(
            "GetOnlineEvaluationConfigResponse.execution_status required"
        )
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError(
            "GetOnlineEvaluationConfigResponse.created_at required"
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
            "GetOnlineEvaluationConfigResponse.updated_at required"
        )
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    return out
