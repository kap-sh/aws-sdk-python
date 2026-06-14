"""Generated from Smithy shape ``com.amazonaws.datazone#ListLineageEventsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.lineage_event_summaries
    import aws_sdk_datazone.types.pagination_token


class ListLineageEventsOutput(TypedDict):
    items: NotRequired[
        "aws_sdk_datazone.types.lineage_event_summaries.LineageEventSummaries"
    ]
    """<p>The results of the ListLineageEvents action.</p>"""
    next_token: NotRequired["aws_sdk_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of lineage events is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of lineage events, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListLineageEvents to list the next set of lineage events.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLineageEventsOutput) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_datazone.types.lineage_event_summaries

        out["items"] = aws_sdk_datazone.types.lineage_event_summaries.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListLineageEventsOutput:
    out: ListLineageEventsOutput = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_datazone.types.lineage_event_summaries

        out["items"] = aws_sdk_datazone.types.lineage_event_summaries.deserialize_json(
            data["items"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
