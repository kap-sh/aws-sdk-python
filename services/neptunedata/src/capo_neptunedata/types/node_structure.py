"""Generated from Smithy shape ``com.amazonaws.neptunedata#NodeStructure``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_neptunedata.types.node_properties
    import capo_neptunedata.types.outgoing_edge_labels


class NodeStructure(TypedDict, closed=True):
    count: NotRequired["int"]
    """<p>Number of nodes that have this specific structure.</p>"""
    node_properties: NotRequired[
        "capo_neptunedata.types.node_properties.NodeProperties"
    ]
    """<p>A list of the node properties present in this specific structure.</p>"""
    distinct_outgoing_edge_labels: NotRequired[
        "capo_neptunedata.types.outgoing_edge_labels.OutgoingEdgeLabels"
    ]
    """<p>A list of distinct outgoing edge labels present in this specific structure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodeStructure) -> dict:
    out: dict = {}
    if "count" in value:
        out["count"] = value["count"]
    if "node_properties" in value:
        import capo_neptunedata.types.node_properties

        out["nodeProperties"] = capo_neptunedata.types.node_properties.serialize_json(
            value["node_properties"]
        )
    if "distinct_outgoing_edge_labels" in value:
        import capo_neptunedata.types.outgoing_edge_labels

        out["distinctOutgoingEdgeLabels"] = (
            capo_neptunedata.types.outgoing_edge_labels.serialize_json(
                value["distinct_outgoing_edge_labels"]
            )
        )
    return out


def deserialize_json(data: dict) -> NodeStructure:
    out: NodeStructure = {}  # type: ignore[typeddict-item]
    if "count" in data:
        out["count"] = data["count"]
    if "nodeProperties" in data:
        import capo_neptunedata.types.node_properties

        out["node_properties"] = (
            capo_neptunedata.types.node_properties.deserialize_json(
                data["nodeProperties"]
            )
        )
    if "distinctOutgoingEdgeLabels" in data:
        import capo_neptunedata.types.outgoing_edge_labels

        out["distinct_outgoing_edge_labels"] = (
            capo_neptunedata.types.outgoing_edge_labels.deserialize_json(
                data["distinctOutgoingEdgeLabels"]
            )
        )
    return out
