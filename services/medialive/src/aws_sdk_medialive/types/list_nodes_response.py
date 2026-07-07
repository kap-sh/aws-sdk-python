"""Generated from Smithy shape ``com.amazonaws.medialive#ListNodesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_describe_node_summary
    import aws_sdk_medialive.types.__string


class ListNodesResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Token for the next result."""
    nodes: NotRequired[
        "aws_sdk_medialive.types.__list_of_describe_node_summary.__listOfDescribeNodeSummary"
    ]
    """An array of Nodes that exist in the Cluster."""


# --- restJson1 ser/de ---
def serialize_json(value: ListNodesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "nodes" in value:
        import aws_sdk_medialive.types.__list_of_describe_node_summary

        out["nodes"] = (
            aws_sdk_medialive.types.__list_of_describe_node_summary.serialize_json(
                value["nodes"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListNodesResponse:
    out: ListNodesResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "nodes" in data:
        import aws_sdk_medialive.types.__list_of_describe_node_summary

        out["nodes"] = (
            aws_sdk_medialive.types.__list_of_describe_node_summary.deserialize_json(
                data["nodes"]
            )
        )
    return out
