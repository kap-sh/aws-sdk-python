"""Generated from Smithy shape ``com.amazonaws.connect#SearchQueuesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.approximate_total_count
    import capo_connect.types.next_token2500
    import capo_connect.types.queue_search_summary_list


class SearchQueuesResponse(TypedDict, closed=True):
    queues: NotRequired[
        "capo_connect.types.queue_search_summary_list.QueueSearchSummaryList"
    ]
    """<p>Information about the queues.</p>"""
    next_token: NotRequired["capo_connect.types.next_token2500.NextToken2500"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""
    approximate_total_count: NotRequired[
        "capo_connect.types.approximate_total_count.ApproximateTotalCount"
    ]
    """<p>The total number of queues which matched your search query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchQueuesResponse) -> dict:
    out: dict = {}
    if "queues" in value:
        import capo_connect.types.queue_search_summary_list

        out["Queues"] = capo_connect.types.queue_search_summary_list.serialize_json(
            value["queues"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "approximate_total_count" in value:
        out["ApproximateTotalCount"] = value["approximate_total_count"]
    return out


def deserialize_json(data: dict) -> SearchQueuesResponse:
    out: SearchQueuesResponse = {}  # type: ignore[typeddict-item]
    if "Queues" in data:
        import capo_connect.types.queue_search_summary_list

        out["queues"] = capo_connect.types.queue_search_summary_list.deserialize_json(
            data["Queues"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ApproximateTotalCount" in data:
        out["approximate_total_count"] = data["ApproximateTotalCount"]
    return out
