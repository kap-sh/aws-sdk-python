"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListClustersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_summaries
    import capo_sagemaker.types.next_token


class ListClustersResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the result of the previous <code>ListClusters</code> request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of clusters, use the token in the next request.</p>"""
    cluster_summaries: NotRequired[
        "capo_sagemaker.types.cluster_summaries.ClusterSummaries"
    ]
    """<p>The summaries of listed SageMaker HyperPod clusters.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListClustersResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "cluster_summaries" in value:
        import capo_sagemaker.types.cluster_summaries

        out["ClusterSummaries"] = (
            capo_sagemaker.types.cluster_summaries.serialize_aws_json_1_1(
                value["cluster_summaries"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListClustersResponse:
    out: ListClustersResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ClusterSummaries" in data:
        import capo_sagemaker.types.cluster_summaries

        out["cluster_summaries"] = (
            capo_sagemaker.types.cluster_summaries.deserialize_aws_json_1_1(
                data["ClusterSummaries"]
            )
        )
    return out
