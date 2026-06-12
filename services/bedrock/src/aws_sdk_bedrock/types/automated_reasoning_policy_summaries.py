"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicySummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_summary

AutomatedReasoningPolicySummaries: TypeAlias = list[
    "aws_sdk_bedrock.types.automated_reasoning_policy_summary.AutomatedReasoningPolicySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicySummaries) -> list:
    import aws_sdk_bedrock.types.automated_reasoning_policy_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_policy_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningPolicySummaries:
    import aws_sdk_bedrock.types.automated_reasoning_policy_summary

    out: AutomatedReasoningPolicySummaries = []
    for item in data:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_policy_summary.deserialize_json(
                item
            )
        )
    return out
