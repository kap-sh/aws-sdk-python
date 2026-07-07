"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdateOnlineEvaluationConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.client_token
    import aws_sdk_bedrock_agentcore_control.types.data_source_config
    import aws_sdk_bedrock_agentcore_control.types.evaluation_config_description
    import aws_sdk_bedrock_agentcore_control.types.evaluator_list
    import aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_id
    import aws_sdk_bedrock_agentcore_control.types.online_evaluation_execution_status
    import aws_sdk_bedrock_agentcore_control.types.role_arn
    import aws_sdk_bedrock_agentcore_control.types.rule


class UpdateOnlineEvaluationConfigRequest(TypedDict, closed=True):
    client_token: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    r"""<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>"""
    online_evaluation_config_id: "aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_id.OnlineEvaluationConfigId"
    """<p> The unique identifier of the online evaluation configuration to update. </p>"""
    description: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.evaluation_config_description.EvaluationConfigDescription"
    ]
    """<p> The updated description of the online evaluation configuration. </p>"""
    rule: NotRequired["aws_sdk_bedrock_agentcore_control.types.rule.Rule"]
    """<p> The updated evaluation rule containing sampling configuration, filters, and session settings. </p>"""
    data_source_config: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.data_source_config.DataSourceConfig"
    ]
    """<p> The updated data source configuration specifying CloudWatch log groups and service names to monitor. </p>"""
    evaluators: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.evaluator_list.EvaluatorList"
    ]
    """<p> The updated list of evaluators to apply during online evaluation. </p>"""
    evaluation_execution_role_arn: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.role_arn.RoleArn"
    ]
    """<p> The updated Amazon Resource Name (ARN) of the IAM role used for evaluation execution. </p>"""
    execution_status: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.online_evaluation_execution_status.OnlineEvaluationExecutionStatus"
    ]
    """<p> The updated execution status to enable or disable the online evaluation. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateOnlineEvaluationConfigRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "description" in value:
        out["description"] = value["description"]
    if "rule" in value:
        import aws_sdk_bedrock_agentcore_control.types.rule

        out["rule"] = aws_sdk_bedrock_agentcore_control.types.rule.serialize_json(
            value["rule"]
        )
    if "data_source_config" in value:
        import aws_sdk_bedrock_agentcore_control.types.data_source_config

        out["dataSourceConfig"] = (
            aws_sdk_bedrock_agentcore_control.types.data_source_config.serialize_json(
                value["data_source_config"]
            )
        )
    if "evaluators" in value:
        import aws_sdk_bedrock_agentcore_control.types.evaluator_list

        out["evaluators"] = (
            aws_sdk_bedrock_agentcore_control.types.evaluator_list.serialize_json(
                value["evaluators"]
            )
        )
    if "evaluation_execution_role_arn" in value:
        out["evaluationExecutionRoleArn"] = value["evaluation_execution_role_arn"]
    if "execution_status" in value:
        import aws_sdk_bedrock_agentcore_control.types.online_evaluation_execution_status

        out["executionStatus"] = (
            aws_sdk_bedrock_agentcore_control.types.online_evaluation_execution_status.serialize_json(
                value["execution_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateOnlineEvaluationConfigRequest:
    out: UpdateOnlineEvaluationConfigRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "description" in data:
        out["description"] = data["description"]
    if "rule" in data:
        import aws_sdk_bedrock_agentcore_control.types.rule

        out["rule"] = aws_sdk_bedrock_agentcore_control.types.rule.deserialize_json(
            data["rule"]
        )
    if "dataSourceConfig" in data:
        import aws_sdk_bedrock_agentcore_control.types.data_source_config

        out["data_source_config"] = (
            aws_sdk_bedrock_agentcore_control.types.data_source_config.deserialize_json(
                data["dataSourceConfig"]
            )
        )
    if "evaluators" in data:
        import aws_sdk_bedrock_agentcore_control.types.evaluator_list

        out["evaluators"] = (
            aws_sdk_bedrock_agentcore_control.types.evaluator_list.deserialize_json(
                data["evaluators"]
            )
        )
    if "evaluationExecutionRoleArn" in data:
        out["evaluation_execution_role_arn"] = data["evaluationExecutionRoleArn"]
    if "executionStatus" in data:
        import aws_sdk_bedrock_agentcore_control.types.online_evaluation_execution_status

        out["execution_status"] = (
            aws_sdk_bedrock_agentcore_control.types.online_evaluation_execution_status.deserialize_json(
                data["executionStatus"]
            )
        )
    return out
