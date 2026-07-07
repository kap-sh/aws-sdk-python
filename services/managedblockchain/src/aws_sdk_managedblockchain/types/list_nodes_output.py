"""Generated from Smithy shape ``com.amazonaws.managedblockchain#ListNodesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.node_summary_list
    import aws_sdk_managedblockchain.types.pagination_token


class ListNodesOutput(TypedDict, closed=True):
    nodes: NotRequired[
        "aws_sdk_managedblockchain.types.node_summary_list.NodeSummaryList"
    ]
    """<p>An array of <code>NodeSummary</code> objects that contain configuration properties for each node.</p>"""
    next_token: NotRequired[
        "aws_sdk_managedblockchain.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token that indicates the next set of results to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNodesOutput) -> dict:
    out: dict = {}
    if "nodes" in value:
        import aws_sdk_managedblockchain.types.node_summary_list

        out["Nodes"] = aws_sdk_managedblockchain.types.node_summary_list.serialize_json(
            value["nodes"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListNodesOutput:
    out: ListNodesOutput = {}  # type: ignore[typeddict-item]
    if "Nodes" in data:
        import aws_sdk_managedblockchain.types.node_summary_list

        out["nodes"] = (
            aws_sdk_managedblockchain.types.node_summary_list.deserialize_json(
                data["Nodes"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
