"""Generated from Smithy shape ``com.amazonaws.neptunegraph#EdgeStructure``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_neptune_graph.types.edge_properties


class EdgeStructure(TypedDict, closed=True):
    count: NotRequired["int"]
    """<p>The number of instances of the edge in the graph.</p>"""
    edge_properties: NotRequired[
        "capo_neptune_graph.types.edge_properties.EdgeProperties"
    ]
    """<p>A list of the properties associated with the edge.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EdgeStructure) -> dict:
    out: dict = {}
    if "count" in value:
        out["count"] = value["count"]
    if "edge_properties" in value:
        import capo_neptune_graph.types.edge_properties

        out["edgeProperties"] = capo_neptune_graph.types.edge_properties.serialize_json(
            value["edge_properties"]
        )
    return out


def deserialize_json(data: dict) -> EdgeStructure:
    out: EdgeStructure = {}  # type: ignore[typeddict-item]
    if "count" in data:
        out["count"] = data["count"]
    if "edgeProperties" in data:
        import capo_neptune_graph.types.edge_properties

        out["edge_properties"] = (
            capo_neptune_graph.types.edge_properties.deserialize_json(
                data["edgeProperties"]
            )
        )
    return out
