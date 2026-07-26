"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_summary

ClusterSummaries: TypeAlias = list[
    "capo_sagemaker.types.cluster_summary.ClusterSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterSummaries) -> list:
    import capo_sagemaker.types.cluster_summary

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.cluster_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ClusterSummaries:
    import capo_sagemaker.types.cluster_summary

    out: ClusterSummaries = []
    for item in data:
        out.append(capo_sagemaker.types.cluster_summary.deserialize_aws_json_1_1(item))
    return out
