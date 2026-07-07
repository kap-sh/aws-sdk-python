"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ListGraphsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_neptune_graph.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.graph_summary_list
    import aws_sdk_neptune_graph.types.pagination_token


class ListGraphsOutput(TypedDict, closed=True):
    graphs: "aws_sdk_neptune_graph.types.graph_summary_list.GraphSummaryList"
    """<p>A list of the graphs.</p>"""
    next_token: NotRequired[
        "aws_sdk_neptune_graph.types.pagination_token.PaginationToken"
    ]
    """<p>Pagination token used to paginate output.</p> <p>When this value is provided as input, the service returns results from where the previous response left off. When this value is present in output, it indicates that there are more results to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGraphsOutput) -> dict:
    out: dict = {}
    import aws_sdk_neptune_graph.types.graph_summary_list

    out["graphs"] = aws_sdk_neptune_graph.types.graph_summary_list.serialize_json(
        value["graphs"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListGraphsOutput:
    out: ListGraphsOutput = {}  # type: ignore[typeddict-item]
    if "graphs" in data:
        import aws_sdk_neptune_graph.types.graph_summary_list

        out["graphs"] = aws_sdk_neptune_graph.types.graph_summary_list.deserialize_json(
            data["graphs"]
        )
    else:
        raise DeserializationError("ListGraphsOutput.graphs required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
