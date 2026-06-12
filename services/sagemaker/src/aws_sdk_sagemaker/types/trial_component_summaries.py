"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrialComponentSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.trial_component_summary

TrialComponentSummaries: TypeAlias = list[
    "aws_sdk_sagemaker.types.trial_component_summary.TrialComponentSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrialComponentSummaries) -> list:
    import aws_sdk_sagemaker.types.trial_component_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.trial_component_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TrialComponentSummaries:
    import aws_sdk_sagemaker.types.trial_component_summary

    out: TrialComponentSummaries = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.trial_component_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
