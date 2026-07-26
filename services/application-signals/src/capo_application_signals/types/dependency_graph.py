"""Generated from Smithy shape ``com.amazonaws.applicationsignals#DependencyGraph``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_signals.types.edges
    import capo_application_signals.types.nodes


class DependencyGraph(TypedDict, closed=True):
    nodes: NotRequired["capo_application_signals.types.nodes.Nodes"]
    """<p>An array of nodes representing the services, resources, or other entities in the dependency graph.</p>"""
    edges: NotRequired["capo_application_signals.types.edges.Edges"]
    """<p>An array of edges representing the connections and relationships between the nodes in the dependency graph.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DependencyGraph) -> dict:
    out: dict = {}
    if "nodes" in value:
        import capo_application_signals.types.nodes

        out["Nodes"] = capo_application_signals.types.nodes.serialize_json(
            value["nodes"]
        )
    if "edges" in value:
        import capo_application_signals.types.edges

        out["Edges"] = capo_application_signals.types.edges.serialize_json(
            value["edges"]
        )
    return out


def deserialize_json(data: dict) -> DependencyGraph:
    out: DependencyGraph = {}  # type: ignore[typeddict-item]
    if "Nodes" in data:
        import capo_application_signals.types.nodes

        out["nodes"] = capo_application_signals.types.nodes.deserialize_json(
            data["Nodes"]
        )
    if "Edges" in data:
        import capo_application_signals.types.edges

        out["edges"] = capo_application_signals.types.edges.deserialize_json(
            data["Edges"]
        )
    return out
