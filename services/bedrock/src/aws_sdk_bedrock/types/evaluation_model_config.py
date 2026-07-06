"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluationModelConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.evaluation_bedrock_model
    import aws_sdk_bedrock.types.evaluation_precomputed_inference_source


class _EvaluationModelConfig_bedrockModel(TypedDict, closed=True):
    bedrockModel: (
        "aws_sdk_bedrock.types.evaluation_bedrock_model.EvaluationBedrockModel"
    )


class _EvaluationModelConfig_precomputedInferenceSource(TypedDict, closed=True):
    precomputedInferenceSource: "aws_sdk_bedrock.types.evaluation_precomputed_inference_source.EvaluationPrecomputedInferenceSource"


EvaluationModelConfig: TypeAlias = (
    _EvaluationModelConfig_bedrockModel
    | _EvaluationModelConfig_precomputedInferenceSource
)


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationModelConfig) -> dict:
    if "bedrockModel" in value:
        import aws_sdk_bedrock.types.evaluation_bedrock_model

        return {
            "bedrockModel": aws_sdk_bedrock.types.evaluation_bedrock_model.serialize_json(
                value["bedrockModel"]
            )
        }
    elif "precomputedInferenceSource" in value:
        import aws_sdk_bedrock.types.evaluation_precomputed_inference_source

        return {
            "precomputedInferenceSource": aws_sdk_bedrock.types.evaluation_precomputed_inference_source.serialize_json(
                value["precomputedInferenceSource"]
            )
        }
    else:
        raise SerializationError("EvaluationModelConfig: no variant present")


def deserialize_json(data: dict) -> EvaluationModelConfig:
    if "bedrockModel" in data:
        import aws_sdk_bedrock.types.evaluation_bedrock_model

        return {
            "bedrockModel": aws_sdk_bedrock.types.evaluation_bedrock_model.deserialize_json(
                data["bedrockModel"]
            )
        }
    elif "precomputedInferenceSource" in data:
        import aws_sdk_bedrock.types.evaluation_precomputed_inference_source

        return {
            "precomputedInferenceSource": aws_sdk_bedrock.types.evaluation_precomputed_inference_source.deserialize_json(
                data["precomputedInferenceSource"]
            )
        }
    else:
        raise DeserializationError("EvaluationModelConfig: no recognized variant key")
