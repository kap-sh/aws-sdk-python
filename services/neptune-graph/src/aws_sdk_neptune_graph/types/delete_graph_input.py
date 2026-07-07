"""Generated from Smithy shape ``com.amazonaws.neptunegraph#DeleteGraphInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.graph_identifier


class DeleteGraphInput(TypedDict, closed=True):
    graph_identifier: "aws_sdk_neptune_graph.types.graph_identifier.GraphIdentifier"
    """<p>The unique identifier of the Neptune Analytics graph.</p>"""
    skip_snapshot: "bool"
    """<p>Determines whether a final graph snapshot is created before the graph is deleted. If <code>true</code> is specified, no graph snapshot is created. If <code>false</code> is specified, a graph snapshot is created before the graph is deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteGraphInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteGraphInput:
    out: DeleteGraphInput = {}  # type: ignore[typeddict-item]
    return out
