"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrialComponentSimpleSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.trial_component_simple_summary

TrialComponentSimpleSummaries: TypeAlias = list[
    "aws_sdk_sagemaker.types.trial_component_simple_summary.TrialComponentSimpleSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrialComponentSimpleSummaries) -> list:
    import aws_sdk_sagemaker.types.trial_component_simple_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.trial_component_simple_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TrialComponentSimpleSummaries:
    import aws_sdk_sagemaker.types.trial_component_simple_summary

    out: TrialComponentSimpleSummaries = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.trial_component_simple_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
