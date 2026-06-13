"""Generated from Smithy shape ``com.amazonaws.neptunegraph#StopGraphInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.graph_identifier


class StopGraphInput(TypedDict):
    graph_identifier: "aws_sdk_neptune_graph.types.graph_identifier.GraphIdentifier"
    """<p>The unique identifier of the Neptune Analytics graph.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopGraphInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopGraphInput:
    out: StopGraphInput = {}  # type: ignore[typeddict-item]
    return out
