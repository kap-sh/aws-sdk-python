"""Generated from Smithy shape ``com.amazonaws.bedrockagent#KnowledgeBaseOrchestrationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.additional_model_request_fields
    import aws_sdk_bedrock_agent.types.knowledge_base_prompt_template
    import aws_sdk_bedrock_agent.types.performance_configuration
    import aws_sdk_bedrock_agent.types.prompt_inference_configuration


class KnowledgeBaseOrchestrationConfiguration(TypedDict, closed=True):
    prompt_template: NotRequired[
        "aws_sdk_bedrock_agent.types.knowledge_base_prompt_template.KnowledgeBasePromptTemplate"
    ]
    """<p>A custom prompt template for orchestrating the retrieval and generation process.</p>"""
    inference_config: NotRequired[
        "aws_sdk_bedrock_agent.types.prompt_inference_configuration.PromptInferenceConfiguration"
    ]
    """<p>Contains inference configurations for the prompt.</p>"""
    additional_model_request_fields: NotRequired[
        "aws_sdk_bedrock_agent.types.additional_model_request_fields.AdditionalModelRequestFields"
    ]
    """<p>The additional model-specific request parameters as key-value pairs to be included in the request to the foundation model.</p>"""
    performance_config: NotRequired[
        "aws_sdk_bedrock_agent.types.performance_configuration.PerformanceConfiguration"
    ]
    """<p>The performance configuration options for the knowledge base retrieval and generation process.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseOrchestrationConfiguration) -> dict:
    out: dict = {}
    if "prompt_template" in value:
        import aws_sdk_bedrock_agent.types.knowledge_base_prompt_template

        out["promptTemplate"] = (
            aws_sdk_bedrock_agent.types.knowledge_base_prompt_template.serialize_json(
                value["prompt_template"]
            )
        )
    if "inference_config" in value:
        import aws_sdk_bedrock_agent.types.prompt_inference_configuration

        out["inferenceConfig"] = (
            aws_sdk_bedrock_agent.types.prompt_inference_configuration.serialize_json(
                value["inference_config"]
            )
        )
    if "additional_model_request_fields" in value:
        import aws_sdk_bedrock_agent.types.additional_model_request_fields

        out["additionalModelRequestFields"] = (
            aws_sdk_bedrock_agent.types.additional_model_request_fields.serialize_json(
                value["additional_model_request_fields"]
            )
        )
    if "performance_config" in value:
        import aws_sdk_bedrock_agent.types.performance_configuration

        out["performanceConfig"] = (
            aws_sdk_bedrock_agent.types.performance_configuration.serialize_json(
                value["performance_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> KnowledgeBaseOrchestrationConfiguration:
    out: KnowledgeBaseOrchestrationConfiguration = {}  # type: ignore[typeddict-item]
    if "promptTemplate" in data:
        import aws_sdk_bedrock_agent.types.knowledge_base_prompt_template

        out["prompt_template"] = (
            aws_sdk_bedrock_agent.types.knowledge_base_prompt_template.deserialize_json(
                data["promptTemplate"]
            )
        )
    if "inferenceConfig" in data:
        import aws_sdk_bedrock_agent.types.prompt_inference_configuration

        out["inference_config"] = (
            aws_sdk_bedrock_agent.types.prompt_inference_configuration.deserialize_json(
                data["inferenceConfig"]
            )
        )
    if "additionalModelRequestFields" in data:
        import aws_sdk_bedrock_agent.types.additional_model_request_fields

        out["additional_model_request_fields"] = (
            aws_sdk_bedrock_agent.types.additional_model_request_fields.deserialize_json(
                data["additionalModelRequestFields"]
            )
        )
    if "performanceConfig" in data:
        import aws_sdk_bedrock_agent.types.performance_configuration

        out["performance_config"] = (
            aws_sdk_bedrock_agent.types.performance_configuration.deserialize_json(
                data["performanceConfig"]
            )
        )
    return out
