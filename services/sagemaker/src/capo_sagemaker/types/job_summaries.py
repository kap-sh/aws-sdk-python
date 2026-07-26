"""Generated from Smithy shape ``com.amazonaws.sagemaker#JobSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.job_summary

JobSummaries: TypeAlias = list["capo_sagemaker.types.job_summary.JobSummary"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobSummaries) -> list:
    import capo_sagemaker.types.job_summary

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.job_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> JobSummaries:
    import capo_sagemaker.types.job_summary

    out: JobSummaries = []
    for item in data:
        out.append(capo_sagemaker.types.job_summary.deserialize_aws_json_1_1(item))
    return out
