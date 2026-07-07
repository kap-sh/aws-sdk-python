"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailUsage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_policies_processed
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_policy_units_processed
    import aws_sdk_bedrock_runtime.types.guardrail_content_policy_image_units_processed
    import aws_sdk_bedrock_runtime.types.guardrail_content_policy_units_processed
    import aws_sdk_bedrock_runtime.types.guardrail_contextual_grounding_policy_units_processed
    import aws_sdk_bedrock_runtime.types.guardrail_sensitive_information_policy_free_units_processed
    import aws_sdk_bedrock_runtime.types.guardrail_sensitive_information_policy_units_processed
    import aws_sdk_bedrock_runtime.types.guardrail_topic_policy_units_processed
    import aws_sdk_bedrock_runtime.types.guardrail_word_policy_units_processed


class GuardrailUsage(TypedDict, closed=True):
    topic_policy_units: "aws_sdk_bedrock_runtime.types.guardrail_topic_policy_units_processed.GuardrailTopicPolicyUnitsProcessed"
    """<p>The topic policy units processed by the guardrail.</p>"""
    content_policy_units: "aws_sdk_bedrock_runtime.types.guardrail_content_policy_units_processed.GuardrailContentPolicyUnitsProcessed"
    """<p>The content policy units processed by the guardrail.</p>"""
    word_policy_units: "aws_sdk_bedrock_runtime.types.guardrail_word_policy_units_processed.GuardrailWordPolicyUnitsProcessed"
    """<p>The word policy units processed by the guardrail.</p>"""
    sensitive_information_policy_units: "aws_sdk_bedrock_runtime.types.guardrail_sensitive_information_policy_units_processed.GuardrailSensitiveInformationPolicyUnitsProcessed"
    """<p>The sensitive information policy units processed by the guardrail.</p>"""
    sensitive_information_policy_free_units: "aws_sdk_bedrock_runtime.types.guardrail_sensitive_information_policy_free_units_processed.GuardrailSensitiveInformationPolicyFreeUnitsProcessed"
    """<p>The sensitive information policy free units processed by the guardrail.</p>"""
    contextual_grounding_policy_units: "aws_sdk_bedrock_runtime.types.guardrail_contextual_grounding_policy_units_processed.GuardrailContextualGroundingPolicyUnitsProcessed"
    """<p>The contextual grounding policy units processed by the guardrail.</p>"""
    content_policy_image_units: NotRequired[
        "aws_sdk_bedrock_runtime.types.guardrail_content_policy_image_units_processed.GuardrailContentPolicyImageUnitsProcessed"
    ]
    """<p>The content policy image units processed by the guardrail.</p>"""
    automated_reasoning_policy_units: NotRequired[
        "aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_policy_units_processed.GuardrailAutomatedReasoningPolicyUnitsProcessed"
    ]
    """<p>The number of text units processed by the automated reasoning policy.</p>"""
    automated_reasoning_policies: NotRequired[
        "aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_policies_processed.GuardrailAutomatedReasoningPoliciesProcessed"
    ]
    """<p>The number of automated reasoning policies that were processed during the guardrail evaluation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailUsage) -> dict:
    out: dict = {}
    out["topicPolicyUnits"] = value["topic_policy_units"]
    out["contentPolicyUnits"] = value["content_policy_units"]
    out["wordPolicyUnits"] = value["word_policy_units"]
    out["sensitiveInformationPolicyUnits"] = value["sensitive_information_policy_units"]
    out["sensitiveInformationPolicyFreeUnits"] = value[
        "sensitive_information_policy_free_units"
    ]
    out["contextualGroundingPolicyUnits"] = value["contextual_grounding_policy_units"]
    if "content_policy_image_units" in value:
        out["contentPolicyImageUnits"] = value["content_policy_image_units"]
    if "automated_reasoning_policy_units" in value:
        out["automatedReasoningPolicyUnits"] = value["automated_reasoning_policy_units"]
    if "automated_reasoning_policies" in value:
        out["automatedReasoningPolicies"] = value["automated_reasoning_policies"]
    return out


def deserialize_json(data: dict) -> GuardrailUsage:
    out: GuardrailUsage = {}  # type: ignore[typeddict-item]
    if "topicPolicyUnits" in data:
        out["topic_policy_units"] = data["topicPolicyUnits"]
    else:
        raise DeserializationError("GuardrailUsage.topic_policy_units required")
    if "contentPolicyUnits" in data:
        out["content_policy_units"] = data["contentPolicyUnits"]
    else:
        raise DeserializationError("GuardrailUsage.content_policy_units required")
    if "wordPolicyUnits" in data:
        out["word_policy_units"] = data["wordPolicyUnits"]
    else:
        raise DeserializationError("GuardrailUsage.word_policy_units required")
    if "sensitiveInformationPolicyUnits" in data:
        out["sensitive_information_policy_units"] = data[
            "sensitiveInformationPolicyUnits"
        ]
    else:
        raise DeserializationError(
            "GuardrailUsage.sensitive_information_policy_units required"
        )
    if "sensitiveInformationPolicyFreeUnits" in data:
        out["sensitive_information_policy_free_units"] = data[
            "sensitiveInformationPolicyFreeUnits"
        ]
    else:
        raise DeserializationError(
            "GuardrailUsage.sensitive_information_policy_free_units required"
        )
    if "contextualGroundingPolicyUnits" in data:
        out["contextual_grounding_policy_units"] = data[
            "contextualGroundingPolicyUnits"
        ]
    else:
        raise DeserializationError(
            "GuardrailUsage.contextual_grounding_policy_units required"
        )
    if "contentPolicyImageUnits" in data:
        out["content_policy_image_units"] = data["contentPolicyImageUnits"]
    if "automatedReasoningPolicyUnits" in data:
        out["automated_reasoning_policy_units"] = data["automatedReasoningPolicyUnits"]
    if "automatedReasoningPolicies" in data:
        out["automated_reasoning_policies"] = data["automatedReasoningPolicies"]
    return out
