"""Generated from Smithy shape ``com.amazonaws.neptunegraph#GetGraphInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.graph_identifier


class GetGraphInput(TypedDict, closed=True):
    graph_identifier: "aws_sdk_neptune_graph.types.graph_identifier.GraphIdentifier"
    """<p>The unique identifier of the Neptune Analytics graph.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGraphInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetGraphInput:
    out: GetGraphInput = {}  # type: ignore[typeddict-item]
    return out
