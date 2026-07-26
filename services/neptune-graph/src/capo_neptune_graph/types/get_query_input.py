"""Generated from Smithy shape ``com.amazonaws.neptunegraph#GetQueryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_neptune_graph.types.graph_identifier


class GetQueryInput(TypedDict, closed=True):
    graph_identifier: "capo_neptune_graph.types.graph_identifier.GraphIdentifier"
    """<p>The unique identifier of the Neptune Analytics graph.</p>"""
    query_id: "str"
    """<p>The ID of the query in question.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetQueryInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetQueryInput:
    out: GetQueryInput = {}  # type: ignore[typeddict-item]
    return out
