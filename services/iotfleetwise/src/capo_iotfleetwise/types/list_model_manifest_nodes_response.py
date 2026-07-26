"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#ListModelManifestNodesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.next_token
    import capo_iotfleetwise.types.nodes


class ListModelManifestNodesResponse(TypedDict, closed=True):
    nodes: NotRequired["capo_iotfleetwise.types.nodes.Nodes"]
    """<p> A list of information about nodes. </p>"""
    next_token: NotRequired["capo_iotfleetwise.types.next_token.nextToken"]
    """<p> The token to retrieve the next set of results, or <code>null</code> if there are no more results. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListModelManifestNodesResponse) -> dict:
    out: dict = {}
    if "nodes" in value:
        import capo_iotfleetwise.types.nodes

        out["nodes"] = capo_iotfleetwise.types.nodes.serialize_aws_json_1_0(
            value["nodes"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListModelManifestNodesResponse:
    out: ListModelManifestNodesResponse = {}  # type: ignore[typeddict-item]
    if "nodes" in data:
        import capo_iotfleetwise.types.nodes

        out["nodes"] = capo_iotfleetwise.types.nodes.deserialize_aws_json_1_0(
            data["nodes"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
