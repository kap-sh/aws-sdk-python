"""Generated from Smithy shape ``com.amazonaws.appmesh#ListVirtualNodesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.virtual_node_list


class ListVirtualNodesOutput(TypedDict, closed=True):
    virtual_nodes: "aws_sdk_app_mesh.types.virtual_node_list.VirtualNodeList"
    """<p>The list of existing virtual nodes for the specified service mesh.</p>"""
    next_token: NotRequired["str"]
    """<p>The <code>nextToken</code> value to include in a future <code>ListVirtualNodes</code> request. When the results of a <code>ListVirtualNodes</code> request exceed <code>limit</code>, you can use this value to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVirtualNodesOutput) -> dict:
    out: dict = {}
    import aws_sdk_app_mesh.types.virtual_node_list

    out["virtualNodes"] = aws_sdk_app_mesh.types.virtual_node_list.serialize_json(
        value["virtual_nodes"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListVirtualNodesOutput:
    out: ListVirtualNodesOutput = {}  # type: ignore[typeddict-item]
    if "virtualNodes" in data:
        import aws_sdk_app_mesh.types.virtual_node_list

        out["virtual_nodes"] = (
            aws_sdk_app_mesh.types.virtual_node_list.deserialize_json(
                data["virtualNodes"]
            )
        )
    else:
        raise DeserializationError("ListVirtualNodesOutput.virtual_nodes required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
