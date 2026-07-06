"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ResetGraphInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_neptune_graph.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.graph_identifier


class ResetGraphInput(TypedDict, closed=True):
    graph_identifier: "aws_sdk_neptune_graph.types.graph_identifier.GraphIdentifier"
    """<p>ID of the graph to reset.</p>"""
    skip_snapshot: "bool"
    """<p>Determines whether a final graph snapshot is created before the graph data is deleted. If set to <code>true</code>, no graph snapshot is created. If set to <code>false</code>, a graph snapshot is created before the data is deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResetGraphInput) -> dict:
    out: dict = {}
    out["skipSnapshot"] = value["skip_snapshot"]
    return out


def deserialize_json(data: dict) -> ResetGraphInput:
    out: ResetGraphInput = {}  # type: ignore[typeddict-item]
    if "skipSnapshot" in data:
        out["skip_snapshot"] = data["skipSnapshot"]
    else:
        raise DeserializationError("ResetGraphInput.skip_snapshot required")
    return out
