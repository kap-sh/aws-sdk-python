"""Generated from Smithy shape ``com.amazonaws.neptunegraph#GraphDataSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_neptune_graph.types.edge_labels
    import capo_neptune_graph.types.edge_structures
    import capo_neptune_graph.types.long_valued_map_list
    import capo_neptune_graph.types.node_labels
    import capo_neptune_graph.types.node_structures


class GraphDataSummary(TypedDict, closed=True):
    num_nodes: NotRequired["int"]
    """<p>The number of nodes in the graph.</p>"""
    num_edges: NotRequired["int"]
    """<p>The number of edges in the graph.</p>"""
    num_node_labels: NotRequired["int"]
    """<p>The number of distinct node labels in the graph.</p>"""
    num_edge_labels: NotRequired["int"]
    """<p>The number of unique edge labels in the graph.</p>"""
    node_labels: NotRequired["capo_neptune_graph.types.node_labels.NodeLabels"]
    """<p>A list of distinct node labels in the graph.</p>"""
    edge_labels: NotRequired["capo_neptune_graph.types.edge_labels.EdgeLabels"]
    """<p>A list of the edge labels in the graph.</p>"""
    num_node_properties: NotRequired["int"]
    """<p>The number of distinct node properties in the graph.</p>"""
    num_edge_properties: NotRequired["int"]
    """<p>The number of edge properties in the graph.</p>"""
    node_properties: NotRequired[
        "capo_neptune_graph.types.long_valued_map_list.LongValuedMapList"
    ]
    """<p>A list of the distinct node properties in the graph, along with the count of nodes where each property is used.</p>"""
    edge_properties: NotRequired[
        "capo_neptune_graph.types.long_valued_map_list.LongValuedMapList"
    ]
    """<p>A list of the distinct edge properties in the graph, along with the count of edges where each property is used.</p>"""
    total_node_property_values: NotRequired["int"]
    """<p>The total number of usages of all node properties.</p>"""
    total_edge_property_values: NotRequired["int"]
    """<p>The total number of usages of all edge properties.</p>"""
    node_structures: NotRequired[
        "capo_neptune_graph.types.node_structures.NodeStructures"
    ]
    """<p>This field is only present when the requested mode is DETAILED. It contains a list of node structures.</p>"""
    edge_structures: NotRequired[
        "capo_neptune_graph.types.edge_structures.EdgeStructures"
    ]
    """<p>This field is only present when the requested mode is DETAILED. It contains a list of edge structures.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GraphDataSummary) -> dict:
    out: dict = {}
    if "num_nodes" in value:
        out["numNodes"] = value["num_nodes"]
    if "num_edges" in value:
        out["numEdges"] = value["num_edges"]
    if "num_node_labels" in value:
        out["numNodeLabels"] = value["num_node_labels"]
    if "num_edge_labels" in value:
        out["numEdgeLabels"] = value["num_edge_labels"]
    if "node_labels" in value:
        import capo_neptune_graph.types.node_labels

        out["nodeLabels"] = capo_neptune_graph.types.node_labels.serialize_json(
            value["node_labels"]
        )
    if "edge_labels" in value:
        import capo_neptune_graph.types.edge_labels

        out["edgeLabels"] = capo_neptune_graph.types.edge_labels.serialize_json(
            value["edge_labels"]
        )
    if "num_node_properties" in value:
        out["numNodeProperties"] = value["num_node_properties"]
    if "num_edge_properties" in value:
        out["numEdgeProperties"] = value["num_edge_properties"]
    if "node_properties" in value:
        import capo_neptune_graph.types.long_valued_map_list

        out["nodeProperties"] = (
            capo_neptune_graph.types.long_valued_map_list.serialize_json(
                value["node_properties"]
            )
        )
    if "edge_properties" in value:
        import capo_neptune_graph.types.long_valued_map_list

        out["edgeProperties"] = (
            capo_neptune_graph.types.long_valued_map_list.serialize_json(
                value["edge_properties"]
            )
        )
    if "total_node_property_values" in value:
        out["totalNodePropertyValues"] = value["total_node_property_values"]
    if "total_edge_property_values" in value:
        out["totalEdgePropertyValues"] = value["total_edge_property_values"]
    if "node_structures" in value:
        import capo_neptune_graph.types.node_structures

        out["nodeStructures"] = capo_neptune_graph.types.node_structures.serialize_json(
            value["node_structures"]
        )
    if "edge_structures" in value:
        import capo_neptune_graph.types.edge_structures

        out["edgeStructures"] = capo_neptune_graph.types.edge_structures.serialize_json(
            value["edge_structures"]
        )
    return out


def deserialize_json(data: dict) -> GraphDataSummary:
    out: GraphDataSummary = {}  # type: ignore[typeddict-item]
    if "numNodes" in data:
        out["num_nodes"] = data["numNodes"]
    if "numEdges" in data:
        out["num_edges"] = data["numEdges"]
    if "numNodeLabels" in data:
        out["num_node_labels"] = data["numNodeLabels"]
    if "numEdgeLabels" in data:
        out["num_edge_labels"] = data["numEdgeLabels"]
    if "nodeLabels" in data:
        import capo_neptune_graph.types.node_labels

        out["node_labels"] = capo_neptune_graph.types.node_labels.deserialize_json(
            data["nodeLabels"]
        )
    if "edgeLabels" in data:
        import capo_neptune_graph.types.edge_labels

        out["edge_labels"] = capo_neptune_graph.types.edge_labels.deserialize_json(
            data["edgeLabels"]
        )
    if "numNodeProperties" in data:
        out["num_node_properties"] = data["numNodeProperties"]
    if "numEdgeProperties" in data:
        out["num_edge_properties"] = data["numEdgeProperties"]
    if "nodeProperties" in data:
        import capo_neptune_graph.types.long_valued_map_list

        out["node_properties"] = (
            capo_neptune_graph.types.long_valued_map_list.deserialize_json(
                data["nodeProperties"]
            )
        )
    if "edgeProperties" in data:
        import capo_neptune_graph.types.long_valued_map_list

        out["edge_properties"] = (
            capo_neptune_graph.types.long_valued_map_list.deserialize_json(
                data["edgeProperties"]
            )
        )
    if "totalNodePropertyValues" in data:
        out["total_node_property_values"] = data["totalNodePropertyValues"]
    if "totalEdgePropertyValues" in data:
        out["total_edge_property_values"] = data["totalEdgePropertyValues"]
    if "nodeStructures" in data:
        import capo_neptune_graph.types.node_structures

        out["node_structures"] = (
            capo_neptune_graph.types.node_structures.deserialize_json(
                data["nodeStructures"]
            )
        )
    if "edgeStructures" in data:
        import capo_neptune_graph.types.edge_structures

        out["edge_structures"] = (
            capo_neptune_graph.types.edge_structures.deserialize_json(
                data["edgeStructures"]
            )
        )
    return out
