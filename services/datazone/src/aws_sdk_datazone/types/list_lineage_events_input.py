"""Generated from Smithy shape ``com.amazonaws.datazone#ListLineageEventsInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.lineage_event_processing_status
    import aws_sdk_datazone.types.max_results
    import aws_sdk_datazone.types.pagination_token
    import aws_sdk_datazone.types.sort_order
    import datetime


class ListLineageEventsInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where you want to list lineage events.</p>"""
    max_results: NotRequired["aws_sdk_datazone.types.max_results.MaxResults"]
    """<p>The maximum number of lineage events to return in a single call to ListLineageEvents. When the number of lineage events to be listed is greater than the value of MaxResults, the response contains a NextToken value that you can use in a subsequent call to ListLineageEvents to list the next set of lineage events.</p>"""
    timestamp_after: NotRequired["datetime.datetime"]
    """<p>The after timestamp of a lineage event.</p>"""
    timestamp_before: NotRequired["datetime.datetime"]
    """<p>The before timestamp of a lineage event.</p>"""
    processing_status: NotRequired[
        "aws_sdk_datazone.types.lineage_event_processing_status.LineageEventProcessingStatus"
    ]
    """<p>The processing status of a lineage event.</p>"""
    sort_order: NotRequired["aws_sdk_datazone.types.sort_order.SortOrder"]
    """<p>The sort order of the lineage events.</p>"""
    next_token: NotRequired["aws_sdk_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of lineage events is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of lineage events, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListLineageEvents to list the next set of lineage events.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLineageEventsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListLineageEventsInput:
    out: ListLineageEventsInput = {}  # type: ignore[typeddict-item]
    return out
