"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateOnlineEvaluationConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.client_token
    import aws_sdk_bedrock_agentcore_control.types.data_source_config
    import aws_sdk_bedrock_agentcore_control.types.evaluation_config_description
    import aws_sdk_bedrock_agentcore_control.types.evaluation_config_name
    import aws_sdk_bedrock_agentcore_control.types.evaluator_list
    import aws_sdk_bedrock_agentcore_control.types.role_arn
    import aws_sdk_bedrock_agentcore_control.types.rule
    import aws_sdk_bedrock_agentcore_control.types.tags_map

class CreateOnlineEvaluationConfigRequest(TypedDict):
    client_token: NotRequired["aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>"""
    online_evaluation_config_name: "aws_sdk_bedrock_agentcore_control.types.evaluation_config_name.EvaluationConfigName"
    """<p> The name of the online evaluation configuration. Must be unique within your account. </p>"""
    description: NotRequired["aws_sdk_bedrock_agentcore_control.types.evaluation_config_description.EvaluationConfigDescription"]
    """<p> The description of the online evaluation configuration that explains its monitoring purpose and scope. </p>"""
    rule: "aws_sdk_bedrock_agentcore_control.types.rule.Rule"
    """<p> The evaluation rule that defines sampling configuration, filters, and session detection settings for the online evaluation. </p>"""
    data_source_config: "aws_sdk_bedrock_agentcore_control.types.data_source_config.DataSourceConfig"
    """<p> The data source configuration that specifies CloudWatch log groups and service names to monitor for agent traces. </p>"""
    evaluators: "aws_sdk_bedrock_agentcore_control.types.evaluator_list.EvaluatorList"
    """<p> The list of evaluators to apply during online evaluation. Can include both built-in evaluators and custom evaluators created with <code>CreateEvaluator</code>. </p>"""
    evaluation_execution_role_arn: "aws_sdk_bedrock_agentcore_control.types.role_arn.RoleArn"
    """<p> The Amazon Resource Name (ARN) of the IAM role that grants permissions to read from CloudWatch logs, write evaluation results, and invoke Amazon Bedrock models for evaluation. If the configuration references evaluators encrypted with a customer managed KMS key, this role must also have <code>kms:Decrypt</code> permission on the KMS key. The service validates this permission at configuration creation time. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations-encryption.html\">Encryption at rest for AgentCore Evaluations</a>. </p>"""
    enable_on_create: "bool"
    """<p> Whether to enable the online evaluation configuration immediately upon creation. If true, evaluation begins automatically. </p>"""
    tags: NotRequired["aws_sdk_bedrock_agentcore_control.types.tags_map.TagsMap"]
    """<p>A map of tag keys and values to assign to an AgentCore Online Evaluation Config. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreateOnlineEvaluationConfigRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["onlineEvaluationConfigName"] = value["online_evaluation_config_name"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_bedrock_agentcore_control.types.rule
    out["rule"] = aws_sdk_bedrock_agentcore_control.types.rule.serialize_json(value["rule"])
    import aws_sdk_bedrock_agentcore_control.types.data_source_config
    out["dataSourceConfig"] = aws_sdk_bedrock_agentcore_control.types.data_source_config.serialize_json(value["data_source_config"])
    import aws_sdk_bedrock_agentcore_control.types.evaluator_list
    out["evaluators"] = aws_sdk_bedrock_agentcore_control.types.evaluator_list.serialize_json(value["evaluators"])
    out["evaluationExecutionRoleArn"] = value["evaluation_execution_role_arn"]
    out["enableOnCreate"] = value["enable_on_create"]
    if "tags" in value:
        import aws_sdk_bedrock_agentcore_control.types.tags_map
        out["tags"] = aws_sdk_bedrock_agentcore_control.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateOnlineEvaluationConfigRequest:
    out: CreateOnlineEvaluationConfigRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "onlineEvaluationConfigName" in data:
        out["online_evaluation_config_name"] = data["onlineEvaluationConfigName"]
    else:
        raise DeserializationError("CreateOnlineEvaluationConfigRequest.online_evaluation_config_name required")
    if "description" in data:
        out["description"] = data["description"]
    if "rule" in data:
        import aws_sdk_bedrock_agentcore_control.types.rule
        out["rule"] = aws_sdk_bedrock_agentcore_control.types.rule.deserialize_json(data["rule"])
    else:
        raise DeserializationError("CreateOnlineEvaluationConfigRequest.rule required")
    if "dataSourceConfig" in data:
        import aws_sdk_bedrock_agentcore_control.types.data_source_config
        out["data_source_config"] = aws_sdk_bedrock_agentcore_control.types.data_source_config.deserialize_json(data["dataSourceConfig"])
    else:
        raise DeserializationError("CreateOnlineEvaluationConfigRequest.data_source_config required")
    if "evaluators" in data:
        import aws_sdk_bedrock_agentcore_control.types.evaluator_list
        out["evaluators"] = aws_sdk_bedrock_agentcore_control.types.evaluator_list.deserialize_json(data["evaluators"])
    else:
        raise DeserializationError("CreateOnlineEvaluationConfigRequest.evaluators required")
    if "evaluationExecutionRoleArn" in data:
        out["evaluation_execution_role_arn"] = data["evaluationExecutionRoleArn"]
    else:
        raise DeserializationError("CreateOnlineEvaluationConfigRequest.evaluation_execution_role_arn required")
    if "enableOnCreate" in data:
        out["enable_on_create"] = data["enableOnCreate"]
    else:
        raise DeserializationError("CreateOnlineEvaluationConfigRequest.enable_on_create required")
    if "tags" in data:
        import aws_sdk_bedrock_agentcore_control.types.tags_map
        out["tags"] = aws_sdk_bedrock_agentcore_control.types.tags_map.deserialize_json(data["tags"])
    return out