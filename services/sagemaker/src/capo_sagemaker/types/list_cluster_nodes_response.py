"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListClusterNodesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_node_summaries
    import capo_sagemaker.types.next_token


class ListClusterNodesResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>The next token specified for listing instances in a SageMaker HyperPod cluster.</p>"""
    cluster_node_summaries: NotRequired[
        "capo_sagemaker.types.cluster_node_summaries.ClusterNodeSummaries"
    ]
    """<p>The summaries of listed instances in a SageMaker HyperPod cluster</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListClusterNodesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "cluster_node_summaries" in value:
        import capo_sagemaker.types.cluster_node_summaries

        out["ClusterNodeSummaries"] = (
            capo_sagemaker.types.cluster_node_summaries.serialize_aws_json_1_1(
                value["cluster_node_summaries"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListClusterNodesResponse:
    out: ListClusterNodesResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ClusterNodeSummaries" in data:
        import capo_sagemaker.types.cluster_node_summaries

        out["cluster_node_summaries"] = (
            capo_sagemaker.types.cluster_node_summaries.deserialize_aws_json_1_1(
                data["ClusterNodeSummaries"]
            )
        )
    return out
