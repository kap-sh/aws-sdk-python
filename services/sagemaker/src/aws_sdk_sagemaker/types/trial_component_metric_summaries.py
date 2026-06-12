"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrialComponentMetricSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.trial_component_metric_summary

TrialComponentMetricSummaries: TypeAlias = list[
    "aws_sdk_sagemaker.types.trial_component_metric_summary.TrialComponentMetricSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrialComponentMetricSummaries) -> list:
    import aws_sdk_sagemaker.types.trial_component_metric_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.trial_component_metric_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TrialComponentMetricSummaries:
    import aws_sdk_sagemaker.types.trial_component_metric_summary

    out: TrialComponentMetricSummaries = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.trial_component_metric_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
