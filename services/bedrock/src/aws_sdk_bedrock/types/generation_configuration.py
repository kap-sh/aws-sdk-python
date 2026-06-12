"""Generated from Smithy shape ``com.amazonaws.bedrock#GenerationConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.additional_model_request_fields
    import aws_sdk_bedrock.types.guardrail_configuration
    import aws_sdk_bedrock.types.kb_inference_config
    import aws_sdk_bedrock.types.prompt_template


class GenerationConfiguration(TypedDict):
    prompt_template: NotRequired["aws_sdk_bedrock.types.prompt_template.PromptTemplate"]
    """<p>Contains the template for the prompt that's sent to the model for response generation.</p>"""
    guardrail_configuration: NotRequired[
        "aws_sdk_bedrock.types.guardrail_configuration.GuardrailConfiguration"
    ]
    """<p>Contains configuration details for the guardrail.</p>"""
    kb_inference_config: NotRequired[
        "aws_sdk_bedrock.types.kb_inference_config.KbInferenceConfig"
    ]
    """<p>Contains configuration details for inference for knowledge base retrieval and response generation.</p>"""
    additional_model_request_fields: NotRequired[
        "aws_sdk_bedrock.types.additional_model_request_fields.AdditionalModelRequestFields"
    ]
    """<p>Additional model parameters and corresponding values not included in the <code>textInferenceConfig</code> structure for a knowledge base. This allows you to provide custom model parameters specific to the language model being used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerationConfiguration) -> dict:
    out: dict = {}
    if "prompt_template" in value:
        import aws_sdk_bedrock.types.prompt_template

        out["promptTemplate"] = aws_sdk_bedrock.types.prompt_template.serialize_json(
            value["prompt_template"]
        )
    if "guardrail_configuration" in value:
        import aws_sdk_bedrock.types.guardrail_configuration

        out["guardrailConfiguration"] = (
            aws_sdk_bedrock.types.guardrail_configuration.serialize_json(
                value["guardrail_configuration"]
            )
        )
    if "kb_inference_config" in value:
        import aws_sdk_bedrock.types.kb_inference_config

        out["kbInferenceConfig"] = (
            aws_sdk_bedrock.types.kb_inference_config.serialize_json(
                value["kb_inference_config"]
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


def deserialize_json(data: dict) -> GenerationConfiguration:
    out: GenerationConfiguration = {}  # type: ignore[typeddict-item]
    if "promptTemplate" in data:
        import aws_sdk_bedrock.types.prompt_template

        out["prompt_template"] = aws_sdk_bedrock.types.prompt_template.deserialize_json(
            data["promptTemplate"]
        )
    if "guardrailConfiguration" in data:
        import aws_sdk_bedrock.types.guardrail_configuration

        out["guardrail_configuration"] = (
            aws_sdk_bedrock.types.guardrail_configuration.deserialize_json(
                data["guardrailConfiguration"]
            )
        )
    if "kbInferenceConfig" in data:
        import aws_sdk_bedrock.types.kb_inference_config

        out["kb_inference_config"] = (
            aws_sdk_bedrock.types.kb_inference_config.deserialize_json(
                data["kbInferenceConfig"]
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
