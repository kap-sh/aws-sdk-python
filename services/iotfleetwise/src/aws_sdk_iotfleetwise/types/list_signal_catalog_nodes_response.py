"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#ListSignalCatalogNodesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.next_token
    import aws_sdk_iotfleetwise.types.nodes


class ListSignalCatalogNodesResponse(TypedDict):
    nodes: NotRequired["aws_sdk_iotfleetwise.types.nodes.Nodes"]
    """<p> A list of information about nodes. </p>"""
    next_token: NotRequired["aws_sdk_iotfleetwise.types.next_token.nextToken"]
    """<p> The token to retrieve the next set of results, or <code>null</code> if there are no more results. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListSignalCatalogNodesResponse) -> dict:
    out: dict = {}
    if "nodes" in value:
        import aws_sdk_iotfleetwise.types.nodes

        out["nodes"] = aws_sdk_iotfleetwise.types.nodes.serialize_aws_json_1_0(
            value["nodes"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListSignalCatalogNodesResponse:
    out: ListSignalCatalogNodesResponse = {}  # type: ignore[typeddict-item]
    if "nodes" in data:
        import aws_sdk_iotfleetwise.types.nodes

        out["nodes"] = aws_sdk_iotfleetwise.types.nodes.deserialize_aws_json_1_0(
            data["nodes"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
