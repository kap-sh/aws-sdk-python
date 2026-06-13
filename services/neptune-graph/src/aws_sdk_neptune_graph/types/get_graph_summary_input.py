"""Generated from Smithy shape ``com.amazonaws.neptunegraph#GetGraphSummaryInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.graph_identifier
    import aws_sdk_neptune_graph.types.graph_summary_mode


class GetGraphSummaryInput(TypedDict):
    graph_identifier: "aws_sdk_neptune_graph.types.graph_identifier.GraphIdentifier"
    """<p>The unique identifier of the Neptune Analytics graph.</p>"""
    mode: NotRequired["aws_sdk_neptune_graph.types.graph_summary_mode.GraphSummaryMode"]
    """<p>The summary mode can take one of two values: <code>basic</code> (the default), and <code>detailed</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGraphSummaryInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetGraphSummaryInput:
    out: GetGraphSummaryInput = {}  # type: ignore[typeddict-item]
    return out
