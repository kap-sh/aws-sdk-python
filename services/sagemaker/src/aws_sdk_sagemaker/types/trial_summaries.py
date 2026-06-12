"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrialSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.trial_summary

TrialSummaries: TypeAlias = list["aws_sdk_sagemaker.types.trial_summary.TrialSummary"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrialSummaries) -> list:
    import aws_sdk_sagemaker.types.trial_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_sagemaker.types.trial_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TrialSummaries:
    import aws_sdk_sagemaker.types.trial_summary

    out: TrialSummaries = []
    for item in data:
        out.append(aws_sdk_sagemaker.types.trial_summary.deserialize_aws_json_1_1(item))
    return out
