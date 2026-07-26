"""Generated from Smithy shape ``com.amazonaws.panorama#ListNodesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.nodes_list
    import capo_panorama.types.token


class ListNodesResponse(TypedDict, closed=True):
    nodes: NotRequired["capo_panorama.types.nodes_list.NodesList"]
    """<p>A list of nodes.</p>"""
    next_token: NotRequired["capo_panorama.types.token.Token"]
    """<p>A pagination token that's included if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNodesResponse) -> dict:
    out: dict = {}
    if "nodes" in value:
        import capo_panorama.types.nodes_list

        out["Nodes"] = capo_panorama.types.nodes_list.serialize_json(value["nodes"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListNodesResponse:
    out: ListNodesResponse = {}  # type: ignore[typeddict-item]
    if "Nodes" in data:
        import capo_panorama.types.nodes_list

        out["nodes"] = capo_panorama.types.nodes_list.deserialize_json(data["Nodes"])
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
