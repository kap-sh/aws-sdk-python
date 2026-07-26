"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ListEventDataStoresRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.list_event_data_stores_max_results_count
    import capo_cloudtrail.types.pagination_token


class ListEventDataStoresRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_cloudtrail.types.pagination_token.PaginationToken"]
    """<p>A token you can use to get the next page of event data store results.</p>"""
    max_results: NotRequired[
        "capo_cloudtrail.types.list_event_data_stores_max_results_count.ListEventDataStoresMaxResultsCount"
    ]
    """<p>The maximum number of event data stores to display on a single page.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEventDataStoresRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEventDataStoresRequest:
    out: ListEventDataStoresRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
