"""Generated from Smithy shape ``com.amazonaws.neptunegraph#CancelQueryInput``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.graph_identifier

class CancelQueryInput(TypedDict):
    graph_identifier: "aws_sdk_neptune_graph.types.graph_identifier.GraphIdentifier"
    """<p>The unique identifier of the Neptune Analytics graph.</p>"""
    query_id: "str"
    """<p>The unique identifier of the query to cancel.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CancelQueryInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelQueryInput:
    out: CancelQueryInput = {}  # type: ignore[typeddict-item]
    return out