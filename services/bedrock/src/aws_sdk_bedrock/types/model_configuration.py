"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.additional_model_request_fields
    import aws_sdk_bedrock.types.bedrock_model_id
    import aws_sdk_bedrock.types.inference_configuration


class ModelConfiguration(TypedDict):
    model_id: "aws_sdk_bedrock.types.bedrock_model_id.BedrockModelId"
    """<p>The ID of the model to use for optimization.</p>"""
    inference_config: NotRequired[
        "aws_sdk_bedrock.types.inference_configuration.InferenceConfiguration"
    ]
    """<p>The inference configuration for the model, including parameters such as maximum tokens, temperature, and top-p.</p>"""
    additional_model_request_fields: NotRequired[
        "aws_sdk_bedrock.types.additional_model_request_fields.AdditionalModelRequestFields"
    ]
    """<p>Additional model request fields. Use this to pass model-specific parameters that are not included in the standard inference configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModelConfiguration) -> dict:
    out: dict = {}
    out["modelId"] = value["model_id"]
    if "inference_config" in value:
        import aws_sdk_bedrock.types.inference_configuration

        out["inferenceConfig"] = (
            aws_sdk_bedrock.types.inference_configuration.serialize_json(
                value["inference_config"]
            )
        )
    if "additional_model_request_fields" in value:
        import aws_sdk_bedrock.types.additional_model_request_fields

        out["additionalModelRequestFields"] = (
            aws_sdk_bedrock.types.additional_model_request_fields.serialize_json(
                value["additional_model_request_fields"]
            )
        )
    return out


def deserialize_json(data: dict) -> ModelConfiguration:
    out: ModelConfiguration = {}  # type: ignore[typeddict-item]
    if "modelId" in data:
        out["model_id"] = data["modelId"]
    else:
        raise DeserializationError("ModelConfiguration.model_id required")
    if "inferenceConfig" in data:
        import aws_sdk_bedrock.types.inference_configuration

        out["inference_config"] = (
            aws_sdk_bedrock.types.inference_configuration.deserialize_json(
                data["inferenceConfig"]
            )
        )
    if "additionalModelRequestFields" in data:
        import aws_sdk_bedrock.types.additional_model_request_fields

        out["additional_model_request_fields"] = (
            aws_sdk_bedrock.types.additional_model_request_fields.deserialize_json(
                data["additionalModelRequestFields"]
            )
        )
    return out
