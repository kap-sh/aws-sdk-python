"""Generated from Smithy shape ``com.amazonaws.finspace#ListKxClusterNodesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_finspace.types.kx_node_summaries
    import aws_sdk_finspace.types.pagination_token


class ListKxClusterNodesResponse(TypedDict):
    nodes: NotRequired["aws_sdk_finspace.types.kx_node_summaries.KxNodeSummaries"]
    """<p>A list of nodes associated with the cluster.</p>"""
    next_token: NotRequired["aws_sdk_finspace.types.pagination_token.PaginationToken"]
    """<p>A token that indicates where a results page should begin.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListKxClusterNodesResponse) -> dict:
    out: dict = {}
    if "nodes" in value:
        import aws_sdk_finspace.types.kx_node_summaries

        out["nodes"] = aws_sdk_finspace.types.kx_node_summaries.serialize_json(
            value["nodes"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListKxClusterNodesResponse:
    out: ListKxClusterNodesResponse = {}  # type: ignore[typeddict-item]
    if "nodes" in data:
        import aws_sdk_finspace.types.kx_node_summaries

        out["nodes"] = aws_sdk_finspace.types.kx_node_summaries.deserialize_json(
            data["nodes"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
