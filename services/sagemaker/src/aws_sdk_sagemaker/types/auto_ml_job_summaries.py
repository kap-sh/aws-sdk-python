"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLJobSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.auto_ml_job_summary

AutoMLJobSummaries: TypeAlias = list[
    "aws_sdk_sagemaker.types.auto_ml_job_summary.AutoMLJobSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLJobSummaries) -> list:
    import aws_sdk_sagemaker.types.auto_ml_job_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.auto_ml_job_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AutoMLJobSummaries:
    import aws_sdk_sagemaker.types.auto_ml_job_summary

    out: AutoMLJobSummaries = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.auto_ml_job_summary.deserialize_aws_json_1_1(item)
        )
    return out
