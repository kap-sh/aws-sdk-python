"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterNodeSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_node_summary

ClusterNodeSummaries: TypeAlias = list[
    "capo_sagemaker.types.cluster_node_summary.ClusterNodeSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterNodeSummaries) -> list:
    import capo_sagemaker.types.cluster_node_summary

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.cluster_node_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ClusterNodeSummaries:
    import capo_sagemaker.types.cluster_node_summary

    out: ClusterNodeSummaries = []
    for item in data:
        out.append(
            capo_sagemaker.types.cluster_node_summary.deserialize_aws_json_1_1(item)
        )
    return out
