"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CodeBasedEvaluatorConfig``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.lambda_evaluator_config


class _CodeBasedEvaluatorConfig_lambdaConfig(TypedDict):
    lambdaConfig: "aws_sdk_bedrock_agentcore_control.types.lambda_evaluator_config.LambdaEvaluatorConfig"


CodeBasedEvaluatorConfig: TypeAlias = _CodeBasedEvaluatorConfig_lambdaConfig


# --- restJson1 ser/de ---
def serialize_json(value: CodeBasedEvaluatorConfig) -> dict:
    if "lambdaConfig" in value:
        import aws_sdk_bedrock_agentcore_control.types.lambda_evaluator_config

        return {
            "lambdaConfig": aws_sdk_bedrock_agentcore_control.types.lambda_evaluator_config.serialize_json(
                value["lambdaConfig"]
            )
        }
    else:
        raise SerializationError("CodeBasedEvaluatorConfig: no variant present")


def deserialize_json(data: dict) -> CodeBasedEvaluatorConfig:
    if "lambdaConfig" in data:
        import aws_sdk_bedrock_agentcore_control.types.lambda_evaluator_config

        return {
            "lambdaConfig": aws_sdk_bedrock_agentcore_control.types.lambda_evaluator_config.deserialize_json(
                data["lambdaConfig"]
            )
        }
    else:
        raise DeserializationError(
            "CodeBasedEvaluatorConfig: no recognized variant key"
        )
