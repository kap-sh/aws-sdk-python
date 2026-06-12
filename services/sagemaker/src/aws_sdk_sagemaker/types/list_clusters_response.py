"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListClustersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_summaries
    import aws_sdk_sagemaker.types.next_token


class ListClustersResponse(TypedDict):
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the result of the previous <code>ListClusters</code> request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of clusters, use the token in the next request.</p>"""
    cluster_summaries: NotRequired[
        "aws_sdk_sagemaker.types.cluster_summaries.ClusterSummaries"
    ]
    """<p>The summaries of listed SageMaker HyperPod clusters.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListClustersResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "cluster_summaries" in value:
        import aws_sdk_sagemaker.types.cluster_summaries

        out["ClusterSummaries"] = (
            aws_sdk_sagemaker.types.cluster_summaries.serialize_aws_json_1_1(
                value["cluster_summaries"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListClustersResponse:
    out: ListClustersResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ClusterSummaries" in data:
        import aws_sdk_sagemaker.types.cluster_summaries

        out["cluster_summaries"] = (
            aws_sdk_sagemaker.types.cluster_summaries.deserialize_aws_json_1_1(
                data["ClusterSummaries"]
            )
        )
    return out
