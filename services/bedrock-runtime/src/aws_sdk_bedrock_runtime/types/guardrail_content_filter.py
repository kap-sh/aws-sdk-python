"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailContentFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_content_filter_confidence
    import aws_sdk_bedrock_runtime.types.guardrail_content_filter_strength
    import aws_sdk_bedrock_runtime.types.guardrail_content_filter_type
    import aws_sdk_bedrock_runtime.types.guardrail_content_policy_action


class GuardrailContentFilter(TypedDict):
    type: "aws_sdk_bedrock_runtime.types.guardrail_content_filter_type.GuardrailContentFilterType"
    """<p>The guardrail type.</p>"""
    confidence: "aws_sdk_bedrock_runtime.types.guardrail_content_filter_confidence.GuardrailContentFilterConfidence"
    """<p>The guardrail confidence.</p>"""
    filter_strength: NotRequired[
        "aws_sdk_bedrock_runtime.types.guardrail_content_filter_strength.GuardrailContentFilterStrength"
    ]
    """<p>The filter strength setting for the guardrail content filter.</p>"""
    action: "aws_sdk_bedrock_runtime.types.guardrail_content_policy_action.GuardrailContentPolicyAction"
    """<p>The guardrail action.</p>"""
    detected: NotRequired["bool"]
    """<p>Indicates whether content that breaches the guardrail configuration is detected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContentFilter) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_runtime.types.guardrail_content_filter_type

    out["type"] = (
        aws_sdk_bedrock_runtime.types.guardrail_content_filter_type.serialize_json(
            value["type"]
        )
    )
    import aws_sdk_bedrock_runtime.types.guardrail_content_filter_confidence

    out["confidence"] = (
        aws_sdk_bedrock_runtime.types.guardrail_content_filter_confidence.serialize_json(
            value["confidence"]
        )
    )
    if "filter_strength" in value:
        import aws_sdk_bedrock_runtime.types.guardrail_content_filter_strength

        out["filterStrength"] = (
            aws_sdk_bedrock_runtime.types.guardrail_content_filter_strength.serialize_json(
                value["filter_strength"]
            )
        )
    import aws_sdk_bedrock_runtime.types.guardrail_content_policy_action

    out["action"] = (
        aws_sdk_bedrock_runtime.types.guardrail_content_policy_action.serialize_json(
            value["action"]
        )
    )
    if "detected" in value:
        out["detected"] = value["detected"]
    return out


def deserialize_json(data: dict) -> GuardrailContentFilter:
    out: GuardrailContentFilter = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_content_filter_type

        out["type"] = (
            aws_sdk_bedrock_runtime.types.guardrail_content_filter_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("GuardrailContentFilter.type required")
    if "confidence" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_content_filter_confidence

        out["confidence"] = (
            aws_sdk_bedrock_runtime.types.guardrail_content_filter_confidence.deserialize_json(
                data["confidence"]
            )
        )
    else:
        raise DeserializationError("GuardrailContentFilter.confidence required")
    if "filterStrength" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_content_filter_strength

        out["filter_strength"] = (
            aws_sdk_bedrock_runtime.types.guardrail_content_filter_strength.deserialize_json(
                data["filterStrength"]
            )
        )
    if "action" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_content_policy_action

        out["action"] = (
            aws_sdk_bedrock_runtime.types.guardrail_content_policy_action.deserialize_json(
                data["action"]
            )
        )
    else:
        raise DeserializationError("GuardrailContentFilter.action required")
    if "detected" in data:
        out["detected"] = data["detected"]
    return out
