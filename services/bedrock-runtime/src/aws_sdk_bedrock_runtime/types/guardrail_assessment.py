"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailAssessment``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.applied_guardrail_details
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_policy_assessment
    import aws_sdk_bedrock_runtime.types.guardrail_content_policy_assessment
    import aws_sdk_bedrock_runtime.types.guardrail_contextual_grounding_policy_assessment
    import aws_sdk_bedrock_runtime.types.guardrail_invocation_metrics
    import aws_sdk_bedrock_runtime.types.guardrail_sensitive_information_policy_assessment
    import aws_sdk_bedrock_runtime.types.guardrail_topic_policy_assessment
    import aws_sdk_bedrock_runtime.types.guardrail_word_policy_assessment


class GuardrailAssessment(TypedDict):
    topic_policy: NotRequired[
        "aws_sdk_bedrock_runtime.types.guardrail_topic_policy_assessment.GuardrailTopicPolicyAssessment"
    ]
    """<p>The topic policy.</p>"""
    content_policy: NotRequired[
        "aws_sdk_bedrock_runtime.types.guardrail_content_policy_assessment.GuardrailContentPolicyAssessment"
    ]
    """<p>The content policy.</p>"""
    word_policy: NotRequired[
        "aws_sdk_bedrock_runtime.types.guardrail_word_policy_assessment.GuardrailWordPolicyAssessment"
    ]
    """<p>The word policy.</p>"""
    sensitive_information_policy: NotRequired[
        "aws_sdk_bedrock_runtime.types.guardrail_sensitive_information_policy_assessment.GuardrailSensitiveInformationPolicyAssessment"
    ]
    """<p>The sensitive information policy.</p>"""
    contextual_grounding_policy: NotRequired[
        "aws_sdk_bedrock_runtime.types.guardrail_contextual_grounding_policy_assessment.GuardrailContextualGroundingPolicyAssessment"
    ]
    """<p>The contextual grounding policy used for the guardrail assessment.</p>"""
    automated_reasoning_policy: NotRequired[
        "aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_policy_assessment.GuardrailAutomatedReasoningPolicyAssessment"
    ]
    """<p>The automated reasoning policy assessment results, including logical validation findings for the input content.</p>"""
    invocation_metrics: NotRequired[
        "aws_sdk_bedrock_runtime.types.guardrail_invocation_metrics.GuardrailInvocationMetrics"
    ]
    """<p>The invocation metrics for the guardrail assessment.</p>"""
    applied_guardrail_details: NotRequired[
        "aws_sdk_bedrock_runtime.types.applied_guardrail_details.AppliedGuardrailDetails"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailAssessment) -> dict:
    out: dict = {}
    if "topic_policy" in value:
        import aws_sdk_bedrock_runtime.types.guardrail_topic_policy_assessment

        out["topicPolicy"] = (
            aws_sdk_bedrock_runtime.types.guardrail_topic_policy_assessment.serialize_json(
                value["topic_policy"]
            )
        )
    if "content_policy" in value:
        import aws_sdk_bedrock_runtime.types.guardrail_content_policy_assessment

        out["contentPolicy"] = (
            aws_sdk_bedrock_runtime.types.guardrail_content_policy_assessment.serialize_json(
                value["content_policy"]
            )
        )
    if "word_policy" in value:
        import aws_sdk_bedrock_runtime.types.guardrail_word_policy_assessment

        out["wordPolicy"] = (
            aws_sdk_bedrock_runtime.types.guardrail_word_policy_assessment.serialize_json(
                value["word_policy"]
            )
        )
    if "sensitive_information_policy" in value:
        import aws_sdk_bedrock_runtime.types.guardrail_sensitive_information_policy_assessment

        out["sensitiveInformationPolicy"] = (
            aws_sdk_bedrock_runtime.types.guardrail_sensitive_information_policy_assessment.serialize_json(
                value["sensitive_information_policy"]
            )
        )
    if "contextual_grounding_policy" in value:
        import aws_sdk_bedrock_runtime.types.guardrail_contextual_grounding_policy_assessment

        out["contextualGroundingPolicy"] = (
            aws_sdk_bedrock_runtime.types.guardrail_contextual_grounding_policy_assessment.serialize_json(
                value["contextual_grounding_policy"]
            )
        )
    if "automated_reasoning_policy" in value:
        import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_policy_assessment

        out["automatedReasoningPolicy"] = (
            aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_policy_assessment.serialize_json(
                value["automated_reasoning_policy"]
            )
        )
    if "invocation_metrics" in value:
        import aws_sdk_bedrock_runtime.types.guardrail_invocation_metrics

        out["invocationMetrics"] = (
            aws_sdk_bedrock_runtime.types.guardrail_invocation_metrics.serialize_json(
                value["invocation_metrics"]
            )
        )
    if "applied_guardrail_details" in value:
        import aws_sdk_bedrock_runtime.types.applied_guardrail_details

        out["appliedGuardrailDetails"] = (
            aws_sdk_bedrock_runtime.types.applied_guardrail_details.serialize_json(
                value["applied_guardrail_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> GuardrailAssessment:
    out: GuardrailAssessment = {}  # type: ignore[typeddict-item]
    if "topicPolicy" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_topic_policy_assessment

        out["topic_policy"] = (
            aws_sdk_bedrock_runtime.types.guardrail_topic_policy_assessment.deserialize_json(
                data["topicPolicy"]
            )
        )
    if "contentPolicy" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_content_policy_assessment

        out["content_policy"] = (
            aws_sdk_bedrock_runtime.types.guardrail_content_policy_assessment.deserialize_json(
                data["contentPolicy"]
            )
        )
    if "wordPolicy" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_word_policy_assessment

        out["word_policy"] = (
            aws_sdk_bedrock_runtime.types.guardrail_word_policy_assessment.deserialize_json(
                data["wordPolicy"]
            )
        )
    if "sensitiveInformationPolicy" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_sensitive_information_policy_assessment

        out["sensitive_information_policy"] = (
            aws_sdk_bedrock_runtime.types.guardrail_sensitive_information_policy_assessment.deserialize_json(
                data["sensitiveInformationPolicy"]
            )
        )
    if "contextualGroundingPolicy" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_contextual_grounding_policy_assessment

        out["contextual_grounding_policy"] = (
            aws_sdk_bedrock_runtime.types.guardrail_contextual_grounding_policy_assessment.deserialize_json(
                data["contextualGroundingPolicy"]
            )
        )
    if "automatedReasoningPolicy" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_policy_assessment

        out["automated_reasoning_policy"] = (
            aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_policy_assessment.deserialize_json(
                data["automatedReasoningPolicy"]
            )
        )
    if "invocationMetrics" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_invocation_metrics

        out["invocation_metrics"] = (
            aws_sdk_bedrock_runtime.types.guardrail_invocation_metrics.deserialize_json(
                data["invocationMetrics"]
            )
        )
    if "appliedGuardrailDetails" in data:
        import aws_sdk_bedrock_runtime.types.applied_guardrail_details

        out["applied_guardrail_details"] = (
            aws_sdk_bedrock_runtime.types.applied_guardrail_details.deserialize_json(
                data["appliedGuardrailDetails"]
            )
        )
    return out
