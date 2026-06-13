"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#PreviewResultSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer_automation.types.preview_result_summary

PreviewResultSummaries: TypeAlias = list[
    "aws_sdk_compute_optimizer_automation.types.preview_result_summary.PreviewResultSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PreviewResultSummaries) -> list:
    import aws_sdk_compute_optimizer_automation.types.preview_result_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer_automation.types.preview_result_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> PreviewResultSummaries:
    import aws_sdk_compute_optimizer_automation.types.preview_result_summary

    out: PreviewResultSummaries = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer_automation.types.preview_result_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
