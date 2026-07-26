"""Generated from Smithy shape ``com.amazonaws.managedblockchain#GetNodeOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain.types.node


class GetNodeOutput(TypedDict, closed=True):
    node: NotRequired["capo_managedblockchain.types.node.Node"]
    """<p>Properties of the node configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNodeOutput) -> dict:
    out: dict = {}
    if "node" in value:
        import capo_managedblockchain.types.node

        out["Node"] = capo_managedblockchain.types.node.serialize_json(value["node"])
    return out


def deserialize_json(data: dict) -> GetNodeOutput:
    out: GetNodeOutput = {}  # type: ignore[typeddict-item]
    if "Node" in data:
        import capo_managedblockchain.types.node

        out["node"] = capo_managedblockchain.types.node.deserialize_json(data["Node"])
    return out
