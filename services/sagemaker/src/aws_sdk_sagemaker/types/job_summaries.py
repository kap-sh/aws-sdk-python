"""Generated from Smithy shape ``com.amazonaws.sagemaker#JobSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.job_summary

JobSummaries: TypeAlias = list["aws_sdk_sagemaker.types.job_summary.JobSummary"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobSummaries) -> list:
    import aws_sdk_sagemaker.types.job_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_sagemaker.types.job_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> JobSummaries:
    import aws_sdk_sagemaker.types.job_summary

    out: JobSummaries = []
    for item in data:
        out.append(aws_sdk_sagemaker.types.job_summary.deserialize_aws_json_1_1(item))
    return out
