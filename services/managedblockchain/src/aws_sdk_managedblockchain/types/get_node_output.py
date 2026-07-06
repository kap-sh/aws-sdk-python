"""Generated from Smithy shape ``com.amazonaws.managedblockchain#GetNodeOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.node


class GetNodeOutput(TypedDict, closed=True):
    node: NotRequired["aws_sdk_managedblockchain.types.node.Node"]
    """<p>Properties of the node configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNodeOutput) -> dict:
    out: dict = {}
    if "node" in value:
        import aws_sdk_managedblockchain.types.node

        out["Node"] = aws_sdk_managedblockchain.types.node.serialize_json(value["node"])
    return out


def deserialize_json(data: dict) -> GetNodeOutput:
    out: GetNodeOutput = {}  # type: ignore[typeddict-item]
    if "Node" in data:
        import aws_sdk_managedblockchain.types.node

        out["node"] = aws_sdk_managedblockchain.types.node.deserialize_json(
            data["Node"]
        )
    return out
