"""Generated from Smithy shape ``com.amazonaws.sagemaker#EdgePackagingJobSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.edge_packaging_job_summary

EdgePackagingJobSummaries: TypeAlias = list[
    "capo_sagemaker.types.edge_packaging_job_summary.EdgePackagingJobSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EdgePackagingJobSummaries) -> list:
    import capo_sagemaker.types.edge_packaging_job_summary

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.edge_packaging_job_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EdgePackagingJobSummaries:
    import capo_sagemaker.types.edge_packaging_job_summary

    out: EdgePackagingJobSummaries = []
    for item in data:
        out.append(
            capo_sagemaker.types.edge_packaging_job_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
