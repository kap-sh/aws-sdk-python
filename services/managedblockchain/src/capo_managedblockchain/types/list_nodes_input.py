"""Generated from Smithy shape ``com.amazonaws.managedblockchain#ListNodesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain.types.node_list_max_results
    import capo_managedblockchain.types.node_status
    import capo_managedblockchain.types.pagination_token
    import capo_managedblockchain.types.resource_id_string


class ListNodesInput(TypedDict, closed=True):
    network_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString"
    """<p>The unique identifier of the network for which to list nodes.</p>"""
    member_id: NotRequired[
        "capo_managedblockchain.types.resource_id_string.ResourceIdString"
    ]
    """<p>The unique identifier of the member who owns the nodes to list.</p> <p>Applies only to Hyperledger Fabric and is required for Hyperledger Fabric.</p>"""
    status: NotRequired["capo_managedblockchain.types.node_status.NodeStatus"]
    """<p>An optional status specifier. If provided, only nodes currently in this status are listed.</p>"""
    max_results: NotRequired[
        "capo_managedblockchain.types.node_list_max_results.NodeListMaxResults"
    ]
    """<p>The maximum number of nodes to list.</p>"""
    next_token: NotRequired[
        "capo_managedblockchain.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token that indicates the next set of results to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNodesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListNodesInput:
    out: ListNodesInput = {}  # type: ignore[typeddict-item]
    return out
