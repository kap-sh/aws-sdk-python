"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ListQueriesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.graph_identifier
    import aws_sdk_neptune_graph.types.query_state_input


class ListQueriesInput(TypedDict, closed=True):
    graph_identifier: "aws_sdk_neptune_graph.types.graph_identifier.GraphIdentifier"
    """<p>The unique identifier of the Neptune Analytics graph.</p>"""
    max_results: "int"
    """<p>The maximum number of results to be fetched by the API.</p>"""
    state: NotRequired["aws_sdk_neptune_graph.types.query_state_input.QueryStateInput"]
    """<p>Filtered list of queries based on state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListQueriesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListQueriesInput:
    out: ListQueriesInput = {}  # type: ignore[typeddict-item]
    return out
