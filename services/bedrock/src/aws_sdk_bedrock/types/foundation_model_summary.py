"""Generated from Smithy shape ``com.amazonaws.bedrock#FoundationModelSummary``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.bedrock_model_id
    import aws_sdk_bedrock.types.branded_name
    import aws_sdk_bedrock.types.foundation_model_arn
    import aws_sdk_bedrock.types.foundation_model_lifecycle
    import aws_sdk_bedrock.types.inference_type_list
    import aws_sdk_bedrock.types.model_customization_list
    import aws_sdk_bedrock.types.model_modality_list


class FoundationModelSummary(TypedDict):
    model_arn: "aws_sdk_bedrock.types.foundation_model_arn.FoundationModelArn"
    """<p>The Amazon Resource Name (ARN) of the foundation model.</p>"""
    model_id: "aws_sdk_bedrock.types.bedrock_model_id.BedrockModelId"
    """<p>The model ID of the foundation model.</p>"""
    model_name: NotRequired["aws_sdk_bedrock.types.branded_name.BrandedName"]
    """<p>The name of the model.</p>"""
    provider_name: NotRequired["aws_sdk_bedrock.types.branded_name.BrandedName"]
    """<p>The model's provider name.</p>"""
    input_modalities: NotRequired[
        "aws_sdk_bedrock.types.model_modality_list.ModelModalityList"
    ]
    """<p>The input modalities that the model supports.</p>"""
    output_modalities: NotRequired[
        "aws_sdk_bedrock.types.model_modality_list.ModelModalityList"
    ]
    """<p>The output modalities that the model supports.</p>"""
    response_streaming_supported: NotRequired["bool"]
    """<p>Indicates whether the model supports streaming.</p>"""
    customizations_supported: NotRequired[
        "aws_sdk_bedrock.types.model_customization_list.ModelCustomizationList"
    ]
    """<p>Whether the model supports fine-tuning or continual pre-training.</p>"""
    inference_types_supported: NotRequired[
        "aws_sdk_bedrock.types.inference_type_list.InferenceTypeList"
    ]
    """<p>The inference types that the model supports.</p>"""
    model_lifecycle: NotRequired[
        "aws_sdk_bedrock.types.foundation_model_lifecycle.FoundationModelLifecycle"
    ]
    """<p>Contains details about whether a model version is available or deprecated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FoundationModelSummary) -> dict:
    out: dict = {}
    out["modelArn"] = value["model_arn"]
    out["modelId"] = value["model_id"]
    if "model_name" in value:
        out["modelName"] = value["model_name"]
    if "provider_name" in value:
        out["providerName"] = value["provider_name"]
    if "input_modalities" in value:
        import aws_sdk_bedrock.types.model_modality_list

        out["inputModalities"] = (
            aws_sdk_bedrock.types.model_modality_list.serialize_json(
                value["input_modalities"]
            )
        )
    if "output_modalities" in value:
        import aws_sdk_bedrock.types.model_modality_list

        out["outputModalities"] = (
            aws_sdk_bedrock.types.model_modality_list.serialize_json(
                value["output_modalities"]
            )
        )
    if "response_streaming_supported" in value:
        out["responseStreamingSupported"] = value["response_streaming_supported"]
    if "customizations_supported" in value:
        import aws_sdk_bedrock.types.model_customization_list

        out["customizationsSupported"] = (
            aws_sdk_bedrock.types.model_customization_list.serialize_json(
                value["customizations_supported"]
            )
        )
    if "inference_types_supported" in value:
        import aws_sdk_bedrock.types.inference_type_list

        out["inferenceTypesSupported"] = (
            aws_sdk_bedrock.types.inference_type_list.serialize_json(
                value["inference_types_supported"]
            )
        )
    if "model_lifecycle" in value:
        import aws_sdk_bedrock.types.foundation_model_lifecycle

        out["modelLifecycle"] = (
            aws_sdk_bedrock.types.foundation_model_lifecycle.serialize_json(
                value["model_lifecycle"]
            )
        )
    return out


def deserialize_json(data: dict) -> FoundationModelSummary:
    out: FoundationModelSummary = {}  # type: ignore[typeddict-item]
    if "modelArn" in data:
        out["model_arn"] = data["modelArn"]
    else:
        raise DeserializationError("FoundationModelSummary.model_arn required")
    if "modelId" in data:
        out["model_id"] = data["modelId"]
    else:
        raise DeserializationError("FoundationModelSummary.model_id required")
    if "modelName" in data:
        out["model_name"] = data["modelName"]
    if "providerName" in data:
        out["provider_name"] = data["providerName"]
    if "inputModalities" in data:
        import aws_sdk_bedrock.types.model_modality_list

        out["input_modalities"] = (
            aws_sdk_bedrock.types.model_modality_list.deserialize_json(
                data["inputModalities"]
            )
        )
    if "outputModalities" in data:
        import aws_sdk_bedrock.types.model_modality_list

        out["output_modalities"] = (
            aws_sdk_bedrock.types.model_modality_list.deserialize_json(
                data["outputModalities"]
            )
        )
    if "responseStreamingSupported" in data:
        out["response_streaming_supported"] = data["responseStreamingSupported"]
    if "customizationsSupported" in data:
        import aws_sdk_bedrock.types.model_customization_list

        out["customizations_supported"] = (
            aws_sdk_bedrock.types.model_customization_list.deserialize_json(
                data["customizationsSupported"]
            )
        )
    if "inferenceTypesSupported" in data:
        import aws_sdk_bedrock.types.inference_type_list

        out["inference_types_supported"] = (
            aws_sdk_bedrock.types.inference_type_list.deserialize_json(
                data["inferenceTypesSupported"]
            )
        )
    if "modelLifecycle" in data:
        import aws_sdk_bedrock.types.foundation_model_lifecycle

        out["model_lifecycle"] = (
            aws_sdk_bedrock.types.foundation_model_lifecycle.deserialize_json(
                data["modelLifecycle"]
            )
        )
    return out
