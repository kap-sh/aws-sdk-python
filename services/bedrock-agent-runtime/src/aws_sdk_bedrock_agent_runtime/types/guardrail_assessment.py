"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GuardrailAssessment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.guardrail_content_policy_assessment
    import aws_sdk_bedrock_agent_runtime.types.guardrail_sensitive_information_policy_assessment
    import aws_sdk_bedrock_agent_runtime.types.guardrail_topic_policy_assessment
    import aws_sdk_bedrock_agent_runtime.types.guardrail_word_policy_assessment


class GuardrailAssessment(TypedDict, closed=True):
    topic_policy: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.guardrail_topic_policy_assessment.GuardrailTopicPolicyAssessment"
    ]
    """<p>Topic policy details of the Guardrail.</p>"""
    content_policy: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.guardrail_content_policy_assessment.GuardrailContentPolicyAssessment"
    ]
    """<p>Content policy details of the Guardrail.</p>"""
    word_policy: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.guardrail_word_policy_assessment.GuardrailWordPolicyAssessment"
    ]
    """<p>Word policy details of the Guardrail.</p>"""
    sensitive_information_policy: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.guardrail_sensitive_information_policy_assessment.GuardrailSensitiveInformationPolicyAssessment"
    ]
    """<p>Sensitive Information policy details of Guardrail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailAssessment) -> dict:
    out: dict = {}
    if "topic_policy" in value:
        import aws_sdk_bedrock_agent_runtime.types.guardrail_topic_policy_assessment

        out["topicPolicy"] = (
            aws_sdk_bedrock_agent_runtime.types.guardrail_topic_policy_assessment.serialize_json(
                value["topic_policy"]
            )
        )
    if "content_policy" in value:
        import aws_sdk_bedrock_agent_runtime.types.guardrail_content_policy_assessment

        out["contentPolicy"] = (
            aws_sdk_bedrock_agent_runtime.types.guardrail_content_policy_assessment.serialize_json(
                value["content_policy"]
            )
        )
    if "word_policy" in value:
        import aws_sdk_bedrock_agent_runtime.types.guardrail_word_policy_assessment

        out["wordPolicy"] = (
            aws_sdk_bedrock_agent_runtime.types.guardrail_word_policy_assessment.serialize_json(
                value["word_policy"]
            )
        )
    if "sensitive_information_policy" in value:
        import aws_sdk_bedrock_agent_runtime.types.guardrail_sensitive_information_policy_assessment

        out["sensitiveInformationPolicy"] = (
            aws_sdk_bedrock_agent_runtime.types.guardrail_sensitive_information_policy_assessment.serialize_json(
                value["sensitive_information_policy"]
            )
        )
    return out


def deserialize_json(data: dict) -> GuardrailAssessment:
    out: GuardrailAssessment = {}  # type: ignore[typeddict-item]
    if "topicPolicy" in data:
        import aws_sdk_bedrock_agent_runtime.types.guardrail_topic_policy_assessment

        out["topic_policy"] = (
            aws_sdk_bedrock_agent_runtime.types.guardrail_topic_policy_assessment.deserialize_json(
                data["topicPolicy"]
            )
        )
    if "contentPolicy" in data:
        import aws_sdk_bedrock_agent_runtime.types.guardrail_content_policy_assessment

        out["content_policy"] = (
            aws_sdk_bedrock_agent_runtime.types.guardrail_content_policy_assessment.deserialize_json(
                data["contentPolicy"]
            )
        )
    if "wordPolicy" in data:
        import aws_sdk_bedrock_agent_runtime.types.guardrail_word_policy_assessment

        out["word_policy"] = (
            aws_sdk_bedrock_agent_runtime.types.guardrail_word_policy_assessment.deserialize_json(
                data["wordPolicy"]
            )
        )
    if "sensitiveInformationPolicy" in data:
        import aws_sdk_bedrock_agent_runtime.types.guardrail_sensitive_information_policy_assessment

        out["sensitive_information_policy"] = (
            aws_sdk_bedrock_agent_runtime.types.guardrail_sensitive_information_policy_assessment.deserialize_json(
                data["sensitiveInformationPolicy"]
            )
        )
    return out
