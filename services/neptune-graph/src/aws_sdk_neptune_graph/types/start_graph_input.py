"""Generated from Smithy shape ``com.amazonaws.neptunegraph#StartGraphInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.graph_identifier


class StartGraphInput(TypedDict, closed=True):
    graph_identifier: "aws_sdk_neptune_graph.types.graph_identifier.GraphIdentifier"
    """<p>The unique identifier of the Neptune Analytics graph.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartGraphInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StartGraphInput:
    out: StartGraphInput = {}  # type: ignore[typeddict-item]
    return out
