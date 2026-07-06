"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateEvaluatorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.client_token
    import aws_sdk_bedrock_agentcore_control.types.custom_evaluator_name
    import aws_sdk_bedrock_agentcore_control.types.evaluator_config
    import aws_sdk_bedrock_agentcore_control.types.evaluator_description
    import aws_sdk_bedrock_agentcore_control.types.evaluator_level
    import aws_sdk_bedrock_agentcore_control.types.kms_key_arn
    import aws_sdk_bedrock_agentcore_control.types.tags_map


class CreateEvaluatorRequest(TypedDict, closed=True):
    client_token: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    r"""<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>"""
    evaluator_name: "aws_sdk_bedrock_agentcore_control.types.custom_evaluator_name.CustomEvaluatorName"
    """<p> The name of the evaluator. Must be unique within your account. </p>"""
    description: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.evaluator_description.EvaluatorDescription"
    ]
    """<p> The description of the evaluator that explains its purpose and evaluation criteria. </p>"""
    evaluator_config: (
        "aws_sdk_bedrock_agentcore_control.types.evaluator_config.EvaluatorConfig"
    )
    """<p> The configuration for the evaluator. Specify either LLM-as-a-Judge settings with instructions, rating scale, and model configuration, or code-based settings with a customer-managed Lambda function. </p>"""
    level: "aws_sdk_bedrock_agentcore_control.types.evaluator_level.EvaluatorLevel"
    """<p> The evaluation level that determines the scope of evaluation. Valid values are <code>TOOL_CALL</code> for individual tool invocations, <code>TRACE</code> for single request-response interactions, or <code>SESSION</code> for entire conversation sessions. </p>"""
    kms_key_arn: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"
    ]
    r"""<p> The Amazon Resource Name (ARN) of a customer managed KMS key to use for encrypting sensitive evaluator data, including instructions and rating scale. If you don't specify a KMS key, the evaluator data is encrypted with an Amazon Web Services owned key. Only symmetric encryption KMS keys are supported. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations-encryption.html\">Encryption at rest for AgentCore Evaluations</a>. </p>"""
    tags: NotRequired["aws_sdk_bedrock_agentcore_control.types.tags_map.TagsMap"]
    """<p>A map of tag keys and values to assign to an AgentCore Evaluator. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEvaluatorRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["evaluatorName"] = value["evaluator_name"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_bedrock_agentcore_control.types.evaluator_config

    out["evaluatorConfig"] = (
        aws_sdk_bedrock_agentcore_control.types.evaluator_config.serialize_json(
            value["evaluator_config"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types.evaluator_level

    out["level"] = (
        aws_sdk_bedrock_agentcore_control.types.evaluator_level.serialize_json(
            value["level"]
        )
    )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "tags" in value:
        import aws_sdk_bedrock_agentcore_control.types.tags_map

        out["tags"] = aws_sdk_bedrock_agentcore_control.types.tags_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateEvaluatorRequest:
    out: CreateEvaluatorRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "evaluatorName" in data:
        out["evaluator_name"] = data["evaluatorName"]
    else:
        raise DeserializationError("CreateEvaluatorRequest.evaluator_name required")
    if "description" in data:
        out["description"] = data["description"]
    if "evaluatorConfig" in data:
        import aws_sdk_bedrock_agentcore_control.types.evaluator_config

        out["evaluator_config"] = (
            aws_sdk_bedrock_agentcore_control.types.evaluator_config.deserialize_json(
                data["evaluatorConfig"]
            )
        )
    else:
        raise DeserializationError("CreateEvaluatorRequest.evaluator_config required")
    if "level" in data:
        import aws_sdk_bedrock_agentcore_control.types.evaluator_level

        out["level"] = (
            aws_sdk_bedrock_agentcore_control.types.evaluator_level.deserialize_json(
                data["level"]
            )
        )
    else:
        raise DeserializationError("CreateEvaluatorRequest.level required")
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if "tags" in data:
        import aws_sdk_bedrock_agentcore_control.types.tags_map

        out["tags"] = aws_sdk_bedrock_agentcore_control.types.tags_map.deserialize_json(
            data["tags"]
        )
    return out
