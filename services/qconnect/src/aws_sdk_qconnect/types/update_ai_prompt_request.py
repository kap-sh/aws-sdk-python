"""Generated from Smithy shape ``com.amazonaws.qconnect#UpdateAIPromptRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.ai_prompt_inference_configuration
    import aws_sdk_qconnect.types.ai_prompt_model_identifier
    import aws_sdk_qconnect.types.ai_prompt_template_configuration
    import aws_sdk_qconnect.types.client_token
    import aws_sdk_qconnect.types.description
    import aws_sdk_qconnect.types.uuid_or_arn
    import aws_sdk_qconnect.types.uuid_or_arn_or_either_with_qualifier
    import aws_sdk_qconnect.types.visibility_status


class UpdateAIPromptRequest(TypedDict, closed=True):
    client_token: NotRequired["aws_sdk_qconnect.types.client_token.ClientToken"]
    r"""<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>..</p>"""
    assistant_id: "aws_sdk_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    ai_prompt_id: "aws_sdk_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier"
    """<p>The identifier of the Amazon Q in Connect AI Prompt.</p>"""
    visibility_status: "aws_sdk_qconnect.types.visibility_status.VisibilityStatus"
    """<p>The visibility status of the Amazon Q in Connect AI prompt.</p>"""
    template_configuration: NotRequired[
        "aws_sdk_qconnect.types.ai_prompt_template_configuration.AIPromptTemplateConfiguration"
    ]
    """<p>The configuration of the prompt template for this AI Prompt.</p>"""
    description: NotRequired["aws_sdk_qconnect.types.description.Description"]
    """<p>The description of the Amazon Q in Connect AI Prompt.</p>"""
    model_id: NotRequired[
        "aws_sdk_qconnect.types.ai_prompt_model_identifier.AIPromptModelIdentifier"
    ]
    r"""<p>The identifier of the model used for this AI Prompt.</p> <note> <p>For information about which models are supported in each Amazon Web Services Region, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/create-ai-prompts.html#cli-create-aiprompt\">Supported models for system/custom prompts</a>.</p> </note>"""
    inference_configuration: NotRequired[
        "aws_sdk_qconnect.types.ai_prompt_inference_configuration.AIPromptInferenceConfiguration"
    ]
    """<p>The updated inference configuration for the AI Prompt.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAIPromptRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["visibilityStatus"] = value["visibility_status"]
    if "template_configuration" in value:
        import aws_sdk_qconnect.types.ai_prompt_template_configuration

        out["templateConfiguration"] = (
            aws_sdk_qconnect.types.ai_prompt_template_configuration.serialize_json(
                value["template_configuration"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "model_id" in value:
        out["modelId"] = value["model_id"]
    if "inference_configuration" in value:
        import aws_sdk_qconnect.types.ai_prompt_inference_configuration

        out["inferenceConfiguration"] = (
            aws_sdk_qconnect.types.ai_prompt_inference_configuration.serialize_json(
                value["inference_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAIPromptRequest:
    out: UpdateAIPromptRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "visibilityStatus" in data:
        out["visibility_status"] = data["visibilityStatus"]
    else:
        raise DeserializationError("UpdateAIPromptRequest.visibility_status required")
    if "templateConfiguration" in data:
        import aws_sdk_qconnect.types.ai_prompt_template_configuration

        out["template_configuration"] = (
            aws_sdk_qconnect.types.ai_prompt_template_configuration.deserialize_json(
                data["templateConfiguration"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "modelId" in data:
        out["model_id"] = data["modelId"]
    if "inferenceConfiguration" in data:
        import aws_sdk_qconnect.types.ai_prompt_inference_configuration

        out["inference_configuration"] = (
            aws_sdk_qconnect.types.ai_prompt_inference_configuration.deserialize_json(
                data["inferenceConfiguration"]
            )
        )
    return out
