"""Generated from Smithy shape ``com.amazonaws.neptunegraph#NodeStructure``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.node_properties
    import aws_sdk_neptune_graph.types.outgoing_edge_labels


class NodeStructure(TypedDict):
    count: NotRequired["int"]
    """<p>The number of instances of this node.</p>"""
    node_properties: NotRequired[
        "aws_sdk_neptune_graph.types.node_properties.NodeProperties"
    ]
    """<p>Properties associated with this node.</p>"""
    distinct_outgoing_edge_labels: NotRequired[
        "aws_sdk_neptune_graph.types.outgoing_edge_labels.OutgoingEdgeLabels"
    ]
    """<p>The outgoing edge labels associated with this node.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodeStructure) -> dict:
    out: dict = {}
    if "count" in value:
        out["count"] = value["count"]
    if "node_properties" in value:
        import aws_sdk_neptune_graph.types.node_properties

        out["nodeProperties"] = (
            aws_sdk_neptune_graph.types.node_properties.serialize_json(
                value["node_properties"]
            )
        )
    if "distinct_outgoing_edge_labels" in value:
        import aws_sdk_neptune_graph.types.outgoing_edge_labels

        out["distinctOutgoingEdgeLabels"] = (
            aws_sdk_neptune_graph.types.outgoing_edge_labels.serialize_json(
                value["distinct_outgoing_edge_labels"]
            )
        )
    return out


def deserialize_json(data: dict) -> NodeStructure:
    out: NodeStructure = {}  # type: ignore[typeddict-item]
    if "count" in data:
        out["count"] = data["count"]
    if "nodeProperties" in data:
        import aws_sdk_neptune_graph.types.node_properties

        out["node_properties"] = (
            aws_sdk_neptune_graph.types.node_properties.deserialize_json(
                data["nodeProperties"]
            )
        )
    if "distinctOutgoingEdgeLabels" in data:
        import aws_sdk_neptune_graph.types.outgoing_edge_labels

        out["distinct_outgoing_edge_labels"] = (
            aws_sdk_neptune_graph.types.outgoing_edge_labels.deserialize_json(
                data["distinctOutgoingEdgeLabels"]
            )
        )
    return out
