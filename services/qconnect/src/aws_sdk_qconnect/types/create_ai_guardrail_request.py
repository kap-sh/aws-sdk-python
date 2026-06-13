"""Generated from Smithy shape ``com.amazonaws.qconnect#CreateAIGuardrailRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.ai_guardrail_blocked_messaging
    import aws_sdk_qconnect.types.ai_guardrail_content_policy_config
    import aws_sdk_qconnect.types.ai_guardrail_contextual_grounding_policy_config
    import aws_sdk_qconnect.types.ai_guardrail_description
    import aws_sdk_qconnect.types.ai_guardrail_sensitive_information_policy_config
    import aws_sdk_qconnect.types.ai_guardrail_topic_policy_config
    import aws_sdk_qconnect.types.ai_guardrail_word_policy_config
    import aws_sdk_qconnect.types.client_token
    import aws_sdk_qconnect.types.name
    import aws_sdk_qconnect.types.tags
    import aws_sdk_qconnect.types.uuid_or_arn
    import aws_sdk_qconnect.types.visibility_status


class CreateAIGuardrailRequest(TypedDict):
    client_token: NotRequired["aws_sdk_qconnect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>..</p>"""
    assistant_id: "aws_sdk_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    name: "aws_sdk_qconnect.types.name.Name"
    """<p>The name of the AI Guardrail.</p>"""
    blocked_input_messaging: "aws_sdk_qconnect.types.ai_guardrail_blocked_messaging.AIGuardrailBlockedMessaging"
    """<p>The message to return when the AI Guardrail blocks a prompt.</p>"""
    blocked_outputs_messaging: "aws_sdk_qconnect.types.ai_guardrail_blocked_messaging.AIGuardrailBlockedMessaging"
    """<p>The message to return when the AI Guardrail blocks a model response.</p>"""
    visibility_status: "aws_sdk_qconnect.types.visibility_status.VisibilityStatus"
    """<p>The visibility status of the AI Guardrail.</p>"""
    description: NotRequired[
        "aws_sdk_qconnect.types.ai_guardrail_description.AIGuardrailDescription"
    ]
    """<p>A description of the AI Guardrail.</p>"""
    topic_policy_config: NotRequired[
        "aws_sdk_qconnect.types.ai_guardrail_topic_policy_config.AIGuardrailTopicPolicyConfig"
    ]
    """<p>The topic policies to configure for the AI Guardrail.</p>"""
    content_policy_config: NotRequired[
        "aws_sdk_qconnect.types.ai_guardrail_content_policy_config.AIGuardrailContentPolicyConfig"
    ]
    """<p>The content filter policies to configure for the AI Guardrail.</p>"""
    word_policy_config: NotRequired[
        "aws_sdk_qconnect.types.ai_guardrail_word_policy_config.AIGuardrailWordPolicyConfig"
    ]
    """<p>The word policy you configure for the AI Guardrail.</p>"""
    sensitive_information_policy_config: NotRequired[
        "aws_sdk_qconnect.types.ai_guardrail_sensitive_information_policy_config.AIGuardrailSensitiveInformationPolicyConfig"
    ]
    """<p>The sensitive information policy to configure for the AI Guardrail.</p>"""
    contextual_grounding_policy_config: NotRequired[
        "aws_sdk_qconnect.types.ai_guardrail_contextual_grounding_policy_config.AIGuardrailContextualGroundingPolicyConfig"
    ]
    """<p>The contextual grounding policy configuration used to create an AI Guardrail.</p>"""
    tags: NotRequired["aws_sdk_qconnect.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAIGuardrailRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["name"] = value["name"]
    out["blockedInputMessaging"] = value["blocked_input_messaging"]
    out["blockedOutputsMessaging"] = value["blocked_outputs_messaging"]
    out["visibilityStatus"] = value["visibility_status"]
    if "description" in value:
        out["description"] = value["description"]
    if "topic_policy_config" in value:
        import aws_sdk_qconnect.types.ai_guardrail_topic_policy_config

        out["topicPolicyConfig"] = (
            aws_sdk_qconnect.types.ai_guardrail_topic_policy_config.serialize_json(
                value["topic_policy_config"]
            )
        )
    if "content_policy_config" in value:
        import aws_sdk_qconnect.types.ai_guardrail_content_policy_config

        out["contentPolicyConfig"] = (
            aws_sdk_qconnect.types.ai_guardrail_content_policy_config.serialize_json(
                value["content_policy_config"]
            )
        )
    if "word_policy_config" in value:
        import aws_sdk_qconnect.types.ai_guardrail_word_policy_config

        out["wordPolicyConfig"] = (
            aws_sdk_qconnect.types.ai_guardrail_word_policy_config.serialize_json(
                value["word_policy_config"]
            )
        )
    if "sensitive_information_policy_config" in value:
        import aws_sdk_qconnect.types.ai_guardrail_sensitive_information_policy_config

        out["sensitiveInformationPolicyConfig"] = (
            aws_sdk_qconnect.types.ai_guardrail_sensitive_information_policy_config.serialize_json(
                value["sensitive_information_policy_config"]
            )
        )
    if "contextual_grounding_policy_config" in value:
        import aws_sdk_qconnect.types.ai_guardrail_contextual_grounding_policy_config

        out["contextualGroundingPolicyConfig"] = (
            aws_sdk_qconnect.types.ai_guardrail_contextual_grounding_policy_config.serialize_json(
                value["contextual_grounding_policy_config"]
            )
        )
    if "tags" in value:
        import aws_sdk_qconnect.types.tags

        out["tags"] = aws_sdk_qconnect.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateAIGuardrailRequest:
    out: CreateAIGuardrailRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateAIGuardrailRequest.name required")
    if "blockedInputMessaging" in data:
        out["blocked_input_messaging"] = data["blockedInputMessaging"]
    else:
        raise DeserializationError(
            "CreateAIGuardrailRequest.blocked_input_messaging required"
        )
    if "blockedOutputsMessaging" in data:
        out["blocked_outputs_messaging"] = data["blockedOutputsMessaging"]
    else:
        raise DeserializationError(
            "CreateAIGuardrailRequest.blocked_outputs_messaging required"
        )
    if "visibilityStatus" in data:
        out["visibility_status"] = data["visibilityStatus"]
    else:
        raise DeserializationError(
            "CreateAIGuardrailRequest.visibility_status required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "topicPolicyConfig" in data:
        import aws_sdk_qconnect.types.ai_guardrail_topic_policy_config

        out["topic_policy_config"] = (
            aws_sdk_qconnect.types.ai_guardrail_topic_policy_config.deserialize_json(
                data["topicPolicyConfig"]
            )
        )
    if "contentPolicyConfig" in data:
        import aws_sdk_qconnect.types.ai_guardrail_content_policy_config

        out["content_policy_config"] = (
            aws_sdk_qconnect.types.ai_guardrail_content_policy_config.deserialize_json(
                data["contentPolicyConfig"]
            )
        )
    if "wordPolicyConfig" in data:
        import aws_sdk_qconnect.types.ai_guardrail_word_policy_config

        out["word_policy_config"] = (
            aws_sdk_qconnect.types.ai_guardrail_word_policy_config.deserialize_json(
                data["wordPolicyConfig"]
            )
        )
    if "sensitiveInformationPolicyConfig" in data:
        import aws_sdk_qconnect.types.ai_guardrail_sensitive_information_policy_config

        out["sensitive_information_policy_config"] = (
            aws_sdk_qconnect.types.ai_guardrail_sensitive_information_policy_config.deserialize_json(
                data["sensitiveInformationPolicyConfig"]
            )
        )
    if "contextualGroundingPolicyConfig" in data:
        import aws_sdk_qconnect.types.ai_guardrail_contextual_grounding_policy_config

        out["contextual_grounding_policy_config"] = (
            aws_sdk_qconnect.types.ai_guardrail_contextual_grounding_policy_config.deserialize_json(
                data["contextualGroundingPolicyConfig"]
            )
        )
    if "tags" in data:
        import aws_sdk_qconnect.types.tags

        out["tags"] = aws_sdk_qconnect.types.tags.deserialize_json(data["tags"])
    return out
