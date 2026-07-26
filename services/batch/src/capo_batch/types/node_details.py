"""Generated from Smithy shape ``com.amazonaws.batch#NodeDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.boolean
    import capo_batch.types.integer


class NodeDetails(TypedDict, closed=True):
    node_index: NotRequired["capo_batch.types.integer.Integer"]
    """<p>The node index for the node. Node index numbering starts at zero. This index is also available on the node with the <code>AWS_BATCH_JOB_NODE_INDEX</code> environment variable.</p>"""
    is_main_node: NotRequired["capo_batch.types.boolean.Boolean"]
    """<p>Specifies whether the current node is the main node for a multi-node parallel job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodeDetails) -> dict:
    out: dict = {}
    if "node_index" in value:
        out["nodeIndex"] = value["node_index"]
    if "is_main_node" in value:
        out["isMainNode"] = value["is_main_node"]
    return out


def deserialize_json(data: dict) -> NodeDetails:
    out: NodeDetails = {}  # type: ignore[typeddict-item]
    if "nodeIndex" in data:
        out["node_index"] = data["nodeIndex"]
    if "isMainNode" in data:
        out["is_main_node"] = data["isMainNode"]
    return out
