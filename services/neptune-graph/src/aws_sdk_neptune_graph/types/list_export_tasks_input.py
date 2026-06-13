"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ListExportTasksInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.graph_identifier
    import aws_sdk_neptune_graph.types.max_results
    import aws_sdk_neptune_graph.types.pagination_token


class ListExportTasksInput(TypedDict):
    graph_identifier: NotRequired[
        "aws_sdk_neptune_graph.types.graph_identifier.GraphIdentifier"
    ]
    """<p>The unique identifier of the Neptune Analytics graph.</p>"""
    next_token: NotRequired[
        "aws_sdk_neptune_graph.types.pagination_token.PaginationToken"
    ]
    """<p>Pagination token used to paginate input.</p>"""
    max_results: NotRequired["aws_sdk_neptune_graph.types.max_results.MaxResults"]
    """<p>The maximum number of export tasks to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListExportTasksInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListExportTasksInput:
    out: ListExportTasksInput = {}  # type: ignore[typeddict-item]
    return out
