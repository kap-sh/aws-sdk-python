"""Generated from Smithy shape ``com.amazonaws.neptunedata#EdgeStructure``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_neptunedata.types.edge_properties

class EdgeStructure(TypedDict):
    count: NotRequired["int"]
    """<p>The number of edges that have this specific structure.</p>"""
    edge_properties: NotRequired["aws_sdk_neptunedata.types.edge_properties.EdgeProperties"]
    """<p>A list of edge properties present in this specific structure.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: EdgeStructure) -> dict:
    out: dict = {}
    if "count" in value:
        out["count"] = value["count"]
    if "edge_properties" in value:
        import aws_sdk_neptunedata.types.edge_properties
        out["edgeProperties"] = aws_sdk_neptunedata.types.edge_properties.serialize_json(value["edge_properties"])
    return out


def deserialize_json(data: dict) -> EdgeStructure:
    out: EdgeStructure = {}  # type: ignore[typeddict-item]
    if "count" in data:
        out["count"] = data["count"]
    if "edgeProperties" in data:
        import aws_sdk_neptunedata.types.edge_properties
        out["edge_properties"] = aws_sdk_neptunedata.types.edge_properties.deserialize_json(data["edgeProperties"])
    return out