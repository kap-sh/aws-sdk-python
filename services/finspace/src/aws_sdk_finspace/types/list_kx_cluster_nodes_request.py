"""Generated from Smithy shape ``com.amazonaws.finspace#ListKxClusterNodesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_finspace.types.kx_cluster_name
    import aws_sdk_finspace.types.kx_environment_id
    import aws_sdk_finspace.types.pagination_token
    import aws_sdk_finspace.types.result_limit


class ListKxClusterNodesRequest(TypedDict):
    environment_id: "aws_sdk_finspace.types.kx_environment_id.KxEnvironmentId"
    """<p>A unique identifier for the kdb environment.</p>"""
    cluster_name: "aws_sdk_finspace.types.kx_cluster_name.KxClusterName"
    """<p>A unique name for the cluster.</p>"""
    next_token: NotRequired["aws_sdk_finspace.types.pagination_token.PaginationToken"]
    """<p>A token that indicates where a results page should begin.</p>"""
    max_results: "aws_sdk_finspace.types.result_limit.ResultLimit"
    """<p>The maximum number of results to return in this request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListKxClusterNodesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListKxClusterNodesRequest:
    out: ListKxClusterNodesRequest = {}  # type: ignore[typeddict-item]
    return out
