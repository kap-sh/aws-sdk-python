"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ListGraphSnapshotsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.graph_identifier
    import aws_sdk_neptune_graph.types.max_results
    import aws_sdk_neptune_graph.types.pagination_token


class ListGraphSnapshotsInput(TypedDict):
    graph_identifier: NotRequired[
        "aws_sdk_neptune_graph.types.graph_identifier.GraphIdentifier"
    ]
    """<p>The unique identifier of the Neptune Analytics graph.</p>"""
    next_token: NotRequired[
        "aws_sdk_neptune_graph.types.pagination_token.PaginationToken"
    ]
    """<p>Pagination token used to paginate output.</p> <p>When this value is provided as input, the service returns results from where the previous response left off. When this value is present in output, it indicates that there are more results to retrieve.</p>"""
    max_results: NotRequired["aws_sdk_neptune_graph.types.max_results.MaxResults"]
    """<p>The total number of records to return in the command's output.</p> <p>If the total number of records available is more than the value specified, <code>nextToken</code> is provided in the command's output. To resume pagination, provide the <code>nextToken</code> output value in the <code>nextToken</code> argument of a subsequent command. Do not use the <code>nextToken</code> response element directly outside of the Amazon CLI.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGraphSnapshotsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListGraphSnapshotsInput:
    out: ListGraphSnapshotsInput = {}  # type: ignore[typeddict-item]
    return out
