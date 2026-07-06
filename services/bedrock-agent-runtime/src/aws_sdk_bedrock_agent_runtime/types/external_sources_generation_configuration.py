"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ExternalSourcesGenerationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.additional_model_request_fields
    import aws_sdk_bedrock_agent_runtime.types.guardrail_configuration
    import aws_sdk_bedrock_agent_runtime.types.inference_config
    import aws_sdk_bedrock_agent_runtime.types.performance_configuration
    import aws_sdk_bedrock_agent_runtime.types.prompt_template


class ExternalSourcesGenerationConfiguration(TypedDict, closed=True):
    prompt_template: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.prompt_template.PromptTemplate"
    ]
    """<p>Contain the textPromptTemplate string for the external source wrapper object.</p>"""
    guardrail_configuration: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.guardrail_configuration.GuardrailConfiguration"
    ]
    """<p>The configuration details for the guardrail.</p>"""
    inference_config: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.inference_config.InferenceConfig"
    ]
    """<p> Configuration settings for inference when using RetrieveAndGenerate to generate responses while using an external source.</p>"""
    additional_model_request_fields: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.additional_model_request_fields.AdditionalModelRequestFields"
    ]
    """<p> Additional model parameters and their corresponding values not included in the textInferenceConfig structure for an external source. Takes in custom model parameters specific to the language model being used. </p>"""
    performance_config: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.performance_configuration.PerformanceConfiguration"
    ]
    """<p>The latency configuration for the model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExternalSourcesGenerationConfiguration) -> dict:
    out: dict = {}
    if "prompt_template" in value:
        import aws_sdk_bedrock_agent_runtime.types.prompt_template

        out["promptTemplate"] = (
            aws_sdk_bedrock_agent_runtime.types.prompt_template.serialize_json(
                value["prompt_template"]
            )
        )
    if "guardrail_configuration" in value:
        import aws_sdk_bedrock_agent_runtime.types.guardrail_configuration

        out["guardrailConfiguration"] = (
            aws_sdk_bedrock_agent_runtime.types.guardrail_configuration.serialize_json(
                value["guardrail_configuration"]
            )
        )
    if "inference_config" in value:
        import aws_sdk_bedrock_agent_runtime.types.inference_config

        out["inferenceConfig"] = (
            aws_sdk_bedrock_agent_runtime.types.inference_config.serialize_json(
                value["inference_config"]
            )
        )
    if "additional_model_request_fields" in value:
        import aws_sdk_bedrock_agent_runtime.types.additional_model_request_fields

        out["additionalModelRequestFields"] = (
            aws_sdk_bedrock_agent_runtime.types.additional_model_request_fields.serialize_json(
                value["additional_model_request_fields"]
            )
        )
    if "performance_config" in value:
        import aws_sdk_bedrock_agent_runtime.types.performance_configuration

        out["performanceConfig"] = (
            aws_sdk_bedrock_agent_runtime.types.performance_configuration.serialize_json(
                value["performance_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExternalSourcesGenerationConfiguration:
    out: ExternalSourcesGenerationConfiguration = {}  # type: ignore[typeddict-item]
    if "promptTemplate" in data:
        import aws_sdk_bedrock_agent_runtime.types.prompt_template

        out["prompt_template"] = (
            aws_sdk_bedrock_agent_runtime.types.prompt_template.deserialize_json(
                data["promptTemplate"]
            )
        )
    if "guardrailConfiguration" in data:
        import aws_sdk_bedrock_agent_runtime.types.guardrail_configuration

        out["guardrail_configuration"] = (
            aws_sdk_bedrock_agent_runtime.types.guardrail_configuration.deserialize_json(
                data["guardrailConfiguration"]
            )
        )
    if "inferenceConfig" in data:
        import aws_sdk_bedrock_agent_runtime.types.inference_config

        out["inference_config"] = (
            aws_sdk_bedrock_agent_runtime.types.inference_config.deserialize_json(
                data["inferenceConfig"]
            )
        )
    if "additionalModelRequestFields" in data:
        import aws_sdk_bedrock_agent_runtime.types.additional_model_request_fields

        out["additional_model_request_fields"] = (
            aws_sdk_bedrock_agent_runtime.types.additional_model_request_fields.deserialize_json(
                data["additionalModelRequestFields"]
            )
        )
    if "performanceConfig" in data:
        import aws_sdk_bedrock_agent_runtime.types.performance_configuration

        out["performance_config"] = (
            aws_sdk_bedrock_agent_runtime.types.performance_configuration.deserialize_json(
                data["performanceConfig"]
            )
        )
    return out
