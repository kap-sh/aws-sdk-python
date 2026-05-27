"""Generated from Smithy shape ``com.amazonaws.eks#DescribeClusterVersionsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.cluster_version_list
    import aws_sdk_eks.types.string


class DescribeClusterVersionsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>Pagination token for the next set of results.</p>"""
    cluster_versions: NotRequired[
        "aws_sdk_eks.types.cluster_version_list.ClusterVersionList"
    ]
    """<p>List of cluster version information objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeClusterVersionsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "cluster_versions" in value:
        import aws_sdk_eks.types.cluster_version_list

        out["clusterVersions"] = aws_sdk_eks.types.cluster_version_list.serialize_json(
            value["cluster_versions"]
        )
    return out


def deserialize_json(data: dict) -> DescribeClusterVersionsResponse:
    out: DescribeClusterVersionsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "clusterVersions" in data:
        import aws_sdk_eks.types.cluster_version_list

        out["cluster_versions"] = (
            aws_sdk_eks.types.cluster_version_list.deserialize_json(
                data["clusterVersions"]
            )
        )
    return out
