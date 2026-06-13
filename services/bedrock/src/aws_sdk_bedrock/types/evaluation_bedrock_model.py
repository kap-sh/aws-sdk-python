"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluationBedrockModel``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.evaluation_bedrock_model_identifier
    import aws_sdk_bedrock.types.evaluation_model_inference_params
    import aws_sdk_bedrock.types.performance_configuration


class EvaluationBedrockModel(TypedDict):
    model_identifier: "aws_sdk_bedrock.types.evaluation_bedrock_model_identifier.EvaluationBedrockModelIdentifier"
    """<p>The ARN of the Amazon Bedrock model or inference profile specified.</p>"""
    inference_params: "aws_sdk_bedrock.types.evaluation_model_inference_params.EvaluationModelInferenceParams"
    """<p>Each Amazon Bedrock support different inference parameters that change how the model behaves during inference.</p>"""
    performance_config: NotRequired[
        "aws_sdk_bedrock.types.performance_configuration.PerformanceConfiguration"
    ]
    """<p>Specifies performance settings for the model or inference profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationBedrockModel) -> dict:
    out: dict = {}
    out["modelIdentifier"] = value["model_identifier"]
    out["inferenceParams"] = value.get("inference_params", "{}")
    if "performance_config" in value:
        import aws_sdk_bedrock.types.performance_configuration

        out["performanceConfig"] = (
            aws_sdk_bedrock.types.performance_configuration.serialize_json(
                value["performance_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluationBedrockModel:
    out: EvaluationBedrockModel = {}  # type: ignore[typeddict-item]
    if "modelIdentifier" in data:
        out["model_identifier"] = data["modelIdentifier"]
    else:
        raise DeserializationError("EvaluationBedrockModel.model_identifier required")
    if "inferenceParams" in data:
        out["inference_params"] = data["inferenceParams"]
    else:
        out["inference_params"] = "{}"
    if "performanceConfig" in data:
        import aws_sdk_bedrock.types.performance_configuration

        out["performance_config"] = (
            aws_sdk_bedrock.types.performance_configuration.deserialize_json(
                data["performanceConfig"]
            )
        )
    return out
