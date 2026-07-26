"""Generated from Smithy shape ``com.amazonaws.sagemaker#TransformJobSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.transform_job_summary

TransformJobSummaries: TypeAlias = list[
    "capo_sagemaker.types.transform_job_summary.TransformJobSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TransformJobSummaries) -> list:
    import capo_sagemaker.types.transform_job_summary

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.transform_job_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TransformJobSummaries:
    import capo_sagemaker.types.transform_job_summary

    out: TransformJobSummaries = []
    for item in data:
        out.append(
            capo_sagemaker.types.transform_job_summary.deserialize_aws_json_1_1(item)
        )
    return out
