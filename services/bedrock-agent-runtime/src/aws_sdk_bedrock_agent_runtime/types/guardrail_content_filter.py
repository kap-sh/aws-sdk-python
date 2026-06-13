"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GuardrailContentFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.guardrail_content_filter_confidence
    import aws_sdk_bedrock_agent_runtime.types.guardrail_content_filter_type
    import aws_sdk_bedrock_agent_runtime.types.guardrail_content_policy_action


class GuardrailContentFilter(TypedDict):
    type: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.guardrail_content_filter_type.GuardrailContentFilterType"
    ]
    """<p>The type of content detected in the filter by the Guardrail.</p>"""
    confidence: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.guardrail_content_filter_confidence.GuardrailContentFilterConfidence"
    ]
    """<p>The confidence level regarding the content detected in the filter by the Guardrail.</p>"""
    action: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.guardrail_content_policy_action.GuardrailContentPolicyAction"
    ]
    """<p>The action placed on the content by the Guardrail filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContentFilter) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_bedrock_agent_runtime.types.guardrail_content_filter_type

        out["type"] = (
            aws_sdk_bedrock_agent_runtime.types.guardrail_content_filter_type.serialize_json(
                value["type"]
            )
        )
    if "confidence" in value:
        import aws_sdk_bedrock_agent_runtime.types.guardrail_content_filter_confidence

        out["confidence"] = (
            aws_sdk_bedrock_agent_runtime.types.guardrail_content_filter_confidence.serialize_json(
                value["confidence"]
            )
        )
    if "action" in value:
        import aws_sdk_bedrock_agent_runtime.types.guardrail_content_policy_action

        out["action"] = (
            aws_sdk_bedrock_agent_runtime.types.guardrail_content_policy_action.serialize_json(
                value["action"]
            )
        )
    return out


def deserialize_json(data: dict) -> GuardrailContentFilter:
    out: GuardrailContentFilter = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_bedrock_agent_runtime.types.guardrail_content_filter_type

        out["type"] = (
            aws_sdk_bedrock_agent_runtime.types.guardrail_content_filter_type.deserialize_json(
                data["type"]
            )
        )
    if "confidence" in data:
        import aws_sdk_bedrock_agent_runtime.types.guardrail_content_filter_confidence

        out["confidence"] = (
            aws_sdk_bedrock_agent_runtime.types.guardrail_content_filter_confidence.deserialize_json(
                data["confidence"]
            )
        )
    if "action" in data:
        import aws_sdk_bedrock_agent_runtime.types.guardrail_content_policy_action

        out["action"] = (
            aws_sdk_bedrock_agent_runtime.types.guardrail_content_policy_action.deserialize_json(
                data["action"]
            )
        )
    return out
