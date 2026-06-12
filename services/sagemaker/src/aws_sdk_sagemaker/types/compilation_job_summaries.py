"""Generated from Smithy shape ``com.amazonaws.sagemaker#CompilationJobSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.compilation_job_summary

CompilationJobSummaries: TypeAlias = list[
    "aws_sdk_sagemaker.types.compilation_job_summary.CompilationJobSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CompilationJobSummaries) -> list:
    import aws_sdk_sagemaker.types.compilation_job_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.compilation_job_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CompilationJobSummaries:
    import aws_sdk_sagemaker.types.compilation_job_summary

    out: CompilationJobSummaries = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.compilation_job_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
