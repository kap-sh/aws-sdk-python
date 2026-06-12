"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailAutomatedReasoningPolicy``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_confidence_filter_threshold
    import aws_sdk_bedrock.types.automated_reasoning_policy_arn_list


class GuardrailAutomatedReasoningPolicy(TypedDict):
    policies: "aws_sdk_bedrock.types.automated_reasoning_policy_arn_list.AutomatedReasoningPolicyArnList"
    """<p>The list of Automated Reasoning policy ARNs that should be applied as part of this guardrail configuration.</p>"""
    confidence_threshold: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_confidence_filter_threshold.AutomatedReasoningConfidenceFilterThreshold"
    ]
    """<p>The minimum confidence level required for Automated Reasoning policy violations to trigger guardrail actions. Values range from 0.0 to 1.0.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailAutomatedReasoningPolicy) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.automated_reasoning_policy_arn_list

    out["policies"] = (
        aws_sdk_bedrock.types.automated_reasoning_policy_arn_list.serialize_json(
            value["policies"]
        )
    )
    if "confidence_threshold" in value:
        out["confidenceThreshold"] = value["confidence_threshold"]
    return out


def deserialize_json(data: dict) -> GuardrailAutomatedReasoningPolicy:
    out: GuardrailAutomatedReasoningPolicy = {}  # type: ignore[typeddict-item]
    if "policies" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_arn_list

        out["policies"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_arn_list.deserialize_json(
                data["policies"]
            )
        )
    else:
        raise DeserializationError(
            "GuardrailAutomatedReasoningPolicy.policies required"
        )
    if "confidenceThreshold" in data:
        out["confidence_threshold"] = data["confidenceThreshold"]
    return out
