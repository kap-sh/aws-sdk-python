"""Generated from Smithy shape ``com.amazonaws.qconnect#AIPromptData``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_qconnect.types.ai_prompt_api_format
    import aws_sdk_qconnect.types.ai_prompt_inference_configuration
    import aws_sdk_qconnect.types.ai_prompt_model_identifier
    import aws_sdk_qconnect.types.ai_prompt_template_configuration
    import aws_sdk_qconnect.types.ai_prompt_template_type
    import aws_sdk_qconnect.types.ai_prompt_type
    import aws_sdk_qconnect.types.arn
    import aws_sdk_qconnect.types.description
    import aws_sdk_qconnect.types.name
    import aws_sdk_qconnect.types.origin
    import aws_sdk_qconnect.types.status
    import aws_sdk_qconnect.types.tags
    import aws_sdk_qconnect.types.uuid
    import aws_sdk_qconnect.types.visibility_status


class AIPromptData(TypedDict):
    assistant_id: "aws_sdk_qconnect.types.uuid.Uuid"
    """<p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    assistant_arn: "aws_sdk_qconnect.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the Amazon Q in Connect assistant.</p>"""
    ai_prompt_id: "aws_sdk_qconnect.types.uuid.Uuid"
    """<p>The identifier of the Amazon Q in Connect AI prompt.</p>"""
    ai_prompt_arn: "aws_sdk_qconnect.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the AI Prompt.</p>"""
    name: "aws_sdk_qconnect.types.name.Name"
    """<p>The name of the AI Prompt</p>"""
    type: "aws_sdk_qconnect.types.ai_prompt_type.AIPromptType"
    """<p>The type of this AI Prompt.</p>"""
    template_type: "aws_sdk_qconnect.types.ai_prompt_template_type.AIPromptTemplateType"
    """<p>The type of the prompt template for this AI Prompt.</p>"""
    model_id: (
        "aws_sdk_qconnect.types.ai_prompt_model_identifier.AIPromptModelIdentifier"
    )
    """<p>The identifier of the model used for this AI Prompt. The following model Ids are supported:</p> <ul> <li> <p> <code>anthropic.claude-3-haiku--v1:0</code> </p> </li> <li> <p> <code>apac.amazon.nova-lite-v1:0</code> </p> </li> <li> <p> <code>apac.amazon.nova-micro-v1:0</code> </p> </li> <li> <p> <code>apac.amazon.nova-pro-v1:0</code> </p> </li> <li> <p> <code>apac.anthropic.claude-3-5-sonnet--v2:0</code> </p> </li> <li> <p> <code>apac.anthropic.claude-3-haiku-20240307-v1:0</code> </p> </li> <li> <p> <code>eu.amazon.nova-lite-v1:0</code> </p> </li> <li> <p> <code>eu.amazon.nova-micro-v1:0</code> </p> </li> <li> <p> <code>eu.amazon.nova-pro-v1:0</code> </p> </li> <li> <p> <code>eu.anthropic.claude-3-7-sonnet-20250219-v1:0</code> </p> </li> <li> <p> <code>eu.anthropic.claude-3-haiku-20240307-v1:0</code> </p> </li> <li> <p> <code>us.amazon.nova-lite-v1:0</code> </p> </li> <li> <p> <code>us.amazon.nova-micro-v1:0</code> </p> </li> <li> <p> <code>us.amazon.nova-pro-v1:0</code> </p> </li> <li> <p> <code>us.anthropic.claude-3-5-haiku-20241022-v1:0</code> </p> </li> <li> <p> <code>us.anthropic.claude-3-7-sonnet-20250219-v1:0</code> </p> </li> <li> <p> <code>us.anthropic.claude-3-haiku-20240307-v1:0</code> </p> </li> </ul>"""
    api_format: "aws_sdk_qconnect.types.ai_prompt_api_format.AIPromptAPIFormat"
    """<p>The API format used for this AI Prompt.</p>"""
    template_configuration: "aws_sdk_qconnect.types.ai_prompt_template_configuration.AIPromptTemplateConfiguration"
    """<p>The configuration of the prompt template for this AI Prompt.</p>"""
    inference_configuration: NotRequired[
        "aws_sdk_qconnect.types.ai_prompt_inference_configuration.AIPromptInferenceConfiguration"
    ]
    """<p>The configuration for inference parameters when using the AI Prompt.</p>"""
    modified_time: NotRequired["datetime.datetime"]
    """<p>The time the AI Prompt was last modified.</p>"""
    description: NotRequired["aws_sdk_qconnect.types.description.Description"]
    """<p>The description of the AI Prompt.</p>"""
    visibility_status: "aws_sdk_qconnect.types.visibility_status.VisibilityStatus"
    """<p>The visibility status of the AI Prompt.</p>"""
    tags: NotRequired["aws_sdk_qconnect.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""
    origin: NotRequired["aws_sdk_qconnect.types.origin.Origin"]
    """<p>The origin of the AI Prompt. <code>SYSTEM</code> for a default AI Prompt created by Q in Connect or <code>CUSTOMER</code> for an AI Prompt created by calling AI Prompt creation APIs. </p>"""
    status: NotRequired["aws_sdk_qconnect.types.status.Status"]
    """<p>The status of the AI Prompt.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AIPromptData) -> dict:
    out: dict = {}
    out["assistantId"] = value["assistant_id"]
    out["assistantArn"] = value["assistant_arn"]
    out["aiPromptId"] = value["ai_prompt_id"]
    out["aiPromptArn"] = value["ai_prompt_arn"]
    out["name"] = value["name"]
    out["type"] = value["type"]
    out["templateType"] = value["template_type"]
    out["modelId"] = value["model_id"]
    out["apiFormat"] = value["api_format"]
    import aws_sdk_qconnect.types.ai_prompt_template_configuration

    out["templateConfiguration"] = (
        aws_sdk_qconnect.types.ai_prompt_template_configuration.serialize_json(
            value["template_configuration"]
        )
    )
    if "inference_configuration" in value:
        import aws_sdk_qconnect.types.ai_prompt_inference_configuration

        out["inferenceConfiguration"] = (
            aws_sdk_qconnect.types.ai_prompt_inference_configuration.serialize_json(
                value["inference_configuration"]
            )
        )
    if "modified_time" in value:
        import aws_sdk_qconnect.types._prelude.timestamp

        out["modifiedTime"] = aws_sdk_qconnect.types._prelude.timestamp.serialize_json(
            value["modified_time"]
        )
    if "description" in value:
        out["description"] = value["description"]
    out["visibilityStatus"] = value["visibility_status"]
    if "tags" in value:
        import aws_sdk_qconnect.types.tags

        out["tags"] = aws_sdk_qconnect.types.tags.serialize_json(value["tags"])
    if "origin" in value:
        out["origin"] = value["origin"]
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> AIPromptData:
    out: AIPromptData = {}  # type: ignore[typeddict-item]
    if "assistantId" in data:
        out["assistant_id"] = data["assistantId"]
    else:
        raise DeserializationError("AIPromptData.assistant_id required")
    if "assistantArn" in data:
        out["assistant_arn"] = data["assistantArn"]
    else:
        raise DeserializationError("AIPromptData.assistant_arn required")
    if "aiPromptId" in data:
        out["ai_prompt_id"] = data["aiPromptId"]
    else:
        raise DeserializationError("AIPromptData.ai_prompt_id required")
    if "aiPromptArn" in data:
        out["ai_prompt_arn"] = data["aiPromptArn"]
    else:
        raise DeserializationError("AIPromptData.ai_prompt_arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AIPromptData.name required")
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("AIPromptData.type required")
    if "templateType" in data:
        out["template_type"] = data["templateType"]
    else:
        raise DeserializationError("AIPromptData.template_type required")
    if "modelId" in data:
        out["model_id"] = data["modelId"]
    else:
        raise DeserializationError("AIPromptData.model_id required")
    if "apiFormat" in data:
        out["api_format"] = data["apiFormat"]
    else:
        raise DeserializationError("AIPromptData.api_format required")
    if "templateConfiguration" in data:
        import aws_sdk_qconnect.types.ai_prompt_template_configuration

        out["template_configuration"] = (
            aws_sdk_qconnect.types.ai_prompt_template_configuration.deserialize_json(
                data["templateConfiguration"]
            )
        )
    else:
        raise DeserializationError("AIPromptData.template_configuration required")
    if "inferenceConfiguration" in data:
        import aws_sdk_qconnect.types.ai_prompt_inference_configuration

        out["inference_configuration"] = (
            aws_sdk_qconnect.types.ai_prompt_inference_configuration.deserialize_json(
                data["inferenceConfiguration"]
            )
        )
    if "modifiedTime" in data:
        import aws_sdk_qconnect.types._prelude.timestamp

        out["modified_time"] = (
            aws_sdk_qconnect.types._prelude.timestamp.deserialize_json(
                data["modifiedTime"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "visibilityStatus" in data:
        out["visibility_status"] = data["visibilityStatus"]
    else:
        raise DeserializationError("AIPromptData.visibility_status required")
    if "tags" in data:
        import aws_sdk_qconnect.types.tags

        out["tags"] = aws_sdk_qconnect.types.tags.deserialize_json(data["tags"])
    if "origin" in data:
        out["origin"] = data["origin"]
    if "status" in data:
        out["status"] = data["status"]
    return out
