"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#RecommendedActionSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer_automation.types.recommended_action_summary

RecommendedActionSummaries: TypeAlias = list[
    "aws_sdk_compute_optimizer_automation.types.recommended_action_summary.RecommendedActionSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecommendedActionSummaries) -> list:
    import aws_sdk_compute_optimizer_automation.types.recommended_action_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer_automation.types.recommended_action_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RecommendedActionSummaries:
    import aws_sdk_compute_optimizer_automation.types.recommended_action_summary

    out: RecommendedActionSummaries = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer_automation.types.recommended_action_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
