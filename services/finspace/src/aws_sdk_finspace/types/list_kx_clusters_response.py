"""Generated from Smithy shape ``com.amazonaws.finspace#ListKxClustersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_finspace.types.kx_clusters
    import aws_sdk_finspace.types.pagination_token


class ListKxClustersResponse(TypedDict):
    kx_cluster_summaries: NotRequired["aws_sdk_finspace.types.kx_clusters.KxClusters"]
    """<p>Lists the cluster details.</p>"""
    next_token: NotRequired["aws_sdk_finspace.types.pagination_token.PaginationToken"]
    """<p>A token that indicates where a results page should begin.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListKxClustersResponse) -> dict:
    out: dict = {}
    if "kx_cluster_summaries" in value:
        import aws_sdk_finspace.types.kx_clusters

        out["kxClusterSummaries"] = aws_sdk_finspace.types.kx_clusters.serialize_json(
            value["kx_cluster_summaries"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListKxClustersResponse:
    out: ListKxClustersResponse = {}  # type: ignore[typeddict-item]
    if "kxClusterSummaries" in data:
        import aws_sdk_finspace.types.kx_clusters

        out["kx_cluster_summaries"] = (
            aws_sdk_finspace.types.kx_clusters.deserialize_json(
                data["kxClusterSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
