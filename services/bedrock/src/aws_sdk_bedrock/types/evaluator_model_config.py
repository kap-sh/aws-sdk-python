"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluatorModelConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.bedrock_evaluator_models


class _EvaluatorModelConfig_bedrockEvaluatorModels(TypedDict, closed=True):
    bedrockEvaluatorModels: (
        "aws_sdk_bedrock.types.bedrock_evaluator_models.BedrockEvaluatorModels"
    )


EvaluatorModelConfig: TypeAlias = _EvaluatorModelConfig_bedrockEvaluatorModels


# --- restJson1 ser/de ---
def serialize_json(value: EvaluatorModelConfig) -> dict:
    if "bedrockEvaluatorModels" in value:
        import aws_sdk_bedrock.types.bedrock_evaluator_models

        return {
            "bedrockEvaluatorModels": aws_sdk_bedrock.types.bedrock_evaluator_models.serialize_json(
                value["bedrockEvaluatorModels"]
            )
        }
    else:
        raise SerializationError("EvaluatorModelConfig: no variant present")


def deserialize_json(data: dict) -> EvaluatorModelConfig:
    if "bedrockEvaluatorModels" in data:
        import aws_sdk_bedrock.types.bedrock_evaluator_models

        return {
            "bedrockEvaluatorModels": aws_sdk_bedrock.types.bedrock_evaluator_models.deserialize_json(
                data["bedrockEvaluatorModels"]
            )
        }
    else:
        raise DeserializationError("EvaluatorModelConfig: no recognized variant key")
