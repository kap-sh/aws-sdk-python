"""Generated from Smithy shape ``com.amazonaws.applicationsignals#DependencyGraph``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.edges
    import aws_sdk_application_signals.types.nodes


class DependencyGraph(TypedDict):
    nodes: NotRequired["aws_sdk_application_signals.types.nodes.Nodes"]
    """<p>An array of nodes representing the services, resources, or other entities in the dependency graph.</p>"""
    edges: NotRequired["aws_sdk_application_signals.types.edges.Edges"]
    """<p>An array of edges representing the connections and relationships between the nodes in the dependency graph.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DependencyGraph) -> dict:
    out: dict = {}
    if "nodes" in value:
        import aws_sdk_application_signals.types.nodes

        out["Nodes"] = aws_sdk_application_signals.types.nodes.serialize_json(
            value["nodes"]
        )
    if "edges" in value:
        import aws_sdk_application_signals.types.edges

        out["Edges"] = aws_sdk_application_signals.types.edges.serialize_json(
            value["edges"]
        )
    return out


def deserialize_json(data: dict) -> DependencyGraph:
    out: DependencyGraph = {}  # type: ignore[typeddict-item]
    if "Nodes" in data:
        import aws_sdk_application_signals.types.nodes

        out["nodes"] = aws_sdk_application_signals.types.nodes.deserialize_json(
            data["Nodes"]
        )
    if "Edges" in data:
        import aws_sdk_application_signals.types.edges

        out["edges"] = aws_sdk_application_signals.types.edges.deserialize_json(
            data["Edges"]
        )
    return out
