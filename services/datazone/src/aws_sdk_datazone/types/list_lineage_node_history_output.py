"""Generated from Smithy shape ``com.amazonaws.datazone#ListLineageNodeHistoryOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.lineage_node_summaries
    import aws_sdk_datazone.types.pagination_token


class ListLineageNodeHistoryOutput(TypedDict, closed=True):
    nodes: NotRequired[
        "aws_sdk_datazone.types.lineage_node_summaries.LineageNodeSummaries"
    ]
    """<p>The nodes returned by the ListLineageNodeHistory action.</p>"""
    next_token: NotRequired["aws_sdk_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of history items is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of items, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListLineageNodeHistory to list the next set of items.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLineageNodeHistoryOutput) -> dict:
    out: dict = {}
    if "nodes" in value:
        import aws_sdk_datazone.types.lineage_node_summaries

        out["nodes"] = aws_sdk_datazone.types.lineage_node_summaries.serialize_json(
            value["nodes"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListLineageNodeHistoryOutput:
    out: ListLineageNodeHistoryOutput = {}  # type: ignore[typeddict-item]
    if "nodes" in data:
        import aws_sdk_datazone.types.lineage_node_summaries

        out["nodes"] = aws_sdk_datazone.types.lineage_node_summaries.deserialize_json(
            data["nodes"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
