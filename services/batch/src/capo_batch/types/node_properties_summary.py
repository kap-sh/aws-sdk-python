"""Generated from Smithy shape ``com.amazonaws.batch#NodePropertiesSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.boolean
    import capo_batch.types.integer


class NodePropertiesSummary(TypedDict, closed=True):
    is_main_node: NotRequired["capo_batch.types.boolean.Boolean"]
    """<p>Specifies whether the current node is the main node for a multi-node parallel job.</p>"""
    num_nodes: NotRequired["capo_batch.types.integer.Integer"]
    """<p>The number of nodes that are associated with a multi-node parallel job.</p>"""
    node_index: NotRequired["capo_batch.types.integer.Integer"]
    """<p>The node index for the node. Node index numbering begins at zero. This index is also available on the node with the <code>AWS_BATCH_JOB_NODE_INDEX</code> environment variable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodePropertiesSummary) -> dict:
    out: dict = {}
    if "is_main_node" in value:
        out["isMainNode"] = value["is_main_node"]
    if "num_nodes" in value:
        out["numNodes"] = value["num_nodes"]
    if "node_index" in value:
        out["nodeIndex"] = value["node_index"]
    return out


def deserialize_json(data: dict) -> NodePropertiesSummary:
    out: NodePropertiesSummary = {}  # type: ignore[typeddict-item]
    if "isMainNode" in data:
        out["is_main_node"] = data["isMainNode"]
    if "numNodes" in data:
        out["num_nodes"] = data["numNodes"]
    if "nodeIndex" in data:
        out["node_index"] = data["nodeIndex"]
    return out
