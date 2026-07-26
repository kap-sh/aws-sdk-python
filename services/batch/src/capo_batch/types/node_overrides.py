"""Generated from Smithy shape ``com.amazonaws.batch#NodeOverrides``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.integer
    import capo_batch.types.node_property_overrides


class NodeOverrides(TypedDict, closed=True):
    num_nodes: NotRequired["capo_batch.types.integer.Integer"]
    """<p>The number of nodes to use with a multi-node parallel job. This value overrides the number of nodes that are specified in the job definition. To use this override, you must meet the following conditions:</p> <ul> <li> <p>There must be at least one node range in your job definition that has an open upper boundary, such as <code>:</code> or <code>n:</code>.</p> </li> <li> <p>The lower boundary of the node range that's specified in the job definition must be fewer than the number of nodes specified in the override.</p> </li> <li> <p>The main node index that's specified in the job definition must be fewer than the number of nodes specified in the override.</p> </li> </ul>"""
    node_property_overrides: NotRequired[
        "capo_batch.types.node_property_overrides.NodePropertyOverrides"
    ]
    """<p>The node property overrides for the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodeOverrides) -> dict:
    out: dict = {}
    if "num_nodes" in value:
        out["numNodes"] = value["num_nodes"]
    if "node_property_overrides" in value:
        import capo_batch.types.node_property_overrides

        out["nodePropertyOverrides"] = (
            capo_batch.types.node_property_overrides.serialize_json(
                value["node_property_overrides"]
            )
        )
    return out


def deserialize_json(data: dict) -> NodeOverrides:
    out: NodeOverrides = {}  # type: ignore[typeddict-item]
    if "numNodes" in data:
        out["num_nodes"] = data["numNodes"]
    if "nodePropertyOverrides" in data:
        import capo_batch.types.node_property_overrides

        out["node_property_overrides"] = (
            capo_batch.types.node_property_overrides.deserialize_json(
                data["nodePropertyOverrides"]
            )
        )
    return out
