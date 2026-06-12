"""Generated from Smithy shape ``com.amazonaws.sagemaker#OptimizationJobSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.optimization_job_summary

OptimizationJobSummaries: TypeAlias = list[
    "aws_sdk_sagemaker.types.optimization_job_summary.OptimizationJobSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OptimizationJobSummaries) -> list:
    import aws_sdk_sagemaker.types.optimization_job_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.optimization_job_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OptimizationJobSummaries:
    import aws_sdk_sagemaker.types.optimization_job_summary

    out: OptimizationJobSummaries = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.optimization_job_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
