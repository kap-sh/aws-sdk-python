"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PromptFlowNodeInlineConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_prompt_model_identifier
    import aws_sdk_bedrock_agent.types.prompt_inference_configuration
    import aws_sdk_bedrock_agent.types.prompt_template_configuration
    import aws_sdk_bedrock_agent.types.prompt_template_type


class PromptFlowNodeInlineConfiguration(TypedDict, closed=True):
    template_type: "aws_sdk_bedrock_agent.types.prompt_template_type.PromptTemplateType"
    """<p>The type of prompt template.</p>"""
    template_configuration: "aws_sdk_bedrock_agent.types.prompt_template_configuration.PromptTemplateConfiguration"
    """<p>Contains a prompt and variables in the prompt that can be replaced with values at runtime.</p>"""
    model_id: "aws_sdk_bedrock_agent.types.flow_prompt_model_identifier.FlowPromptModelIdentifier"
    r"""<p>The unique identifier of the model or <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html\">inference profile</a> to run inference with.</p>"""
    inference_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.prompt_inference_configuration.PromptInferenceConfiguration"
    ]
    """<p>Contains inference configurations for the prompt.</p>"""
    additional_model_request_fields: NotRequired["object"]
    """<p>Additional fields to be included in the model request for the Prompt node.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PromptFlowNodeInlineConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.prompt_template_type

    out["templateType"] = (
        aws_sdk_bedrock_agent.types.prompt_template_type.serialize_json(
            value.get("template_type", "TEXT")
        )
    )
    import aws_sdk_bedrock_agent.types.prompt_template_configuration

    out["templateConfiguration"] = (
        aws_sdk_bedrock_agent.types.prompt_template_configuration.serialize_json(
            value["template_configuration"]
        )
    )
    out["modelId"] = value.get("model_id", "")
    if "inference_configuration" in value:
        import aws_sdk_bedrock_agent.types.prompt_inference_configuration

        out["inferenceConfiguration"] = (
            aws_sdk_bedrock_agent.types.prompt_inference_configuration.serialize_json(
                value["inference_configuration"]
            )
        )
    if "additional_model_request_fields" in value:
        out["additionalModelRequestFields"] = value["additional_model_request_fields"]
    return out


def deserialize_json(data: dict) -> PromptFlowNodeInlineConfiguration:
    out: PromptFlowNodeInlineConfiguration = {}  # type: ignore[typeddict-item]
    if "templateType" in data:
        import aws_sdk_bedrock_agent.types.prompt_template_type

        out["template_type"] = (
            aws_sdk_bedrock_agent.types.prompt_template_type.deserialize_json(
                data["templateType"]
            )
        )
    else:
        out["template_type"] = "TEXT"
    if "templateConfiguration" in data:
        import aws_sdk_bedrock_agent.types.prompt_template_configuration

        out["template_configuration"] = (
            aws_sdk_bedrock_agent.types.prompt_template_configuration.deserialize_json(
                data["templateConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "PromptFlowNodeInlineConfiguration.template_configuration required"
        )
    if "modelId" in data:
        out["model_id"] = data["modelId"]
    else:
        out["model_id"] = ""
    if "inferenceConfiguration" in data:
        import aws_sdk_bedrock_agent.types.prompt_inference_configuration

        out["inference_configuration"] = (
            aws_sdk_bedrock_agent.types.prompt_inference_configuration.deserialize_json(
                data["inferenceConfiguration"]
            )
        )
    if "additionalModelRequestFields" in data:
        out["additional_model_request_fields"] = data["additionalModelRequestFields"]
    return out
