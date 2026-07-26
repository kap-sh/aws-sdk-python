"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProcessingJobSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.processing_job_summary

ProcessingJobSummaries: TypeAlias = list[
    "capo_sagemaker.types.processing_job_summary.ProcessingJobSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProcessingJobSummaries) -> list:
    import capo_sagemaker.types.processing_job_summary

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.processing_job_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ProcessingJobSummaries:
    import capo_sagemaker.types.processing_job_summary

    out: ProcessingJobSummaries = []
    for item in data:
        out.append(
            capo_sagemaker.types.processing_job_summary.deserialize_aws_json_1_1(item)
        )
    return out
