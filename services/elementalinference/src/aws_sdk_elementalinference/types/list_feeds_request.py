"""Generated from Smithy shape ``com.amazonaws.elementalinference#ListFeedsRequest``."""

from typing import TypedDict

from typing_extensions import NotRequired


class ListFeedsRequest(TypedDict):
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return per API request.</p> <p>For example, you submit a list request with MaxResults set at 5. Although 20 items match your request, the service returns no more than the first 5 items. (The service also returns a NextToken value that you can use to fetch the next batch of results.) </p> <p>The service might return fewer results than the MaxResults value. If MaxResults is not included in the request, the service defaults to pagination with a maximum of 10 results per page. </p> <p>Valid Range: Minimum value of 1. Maximum value of 1000.</p>"""
    next_token: NotRequired["str"]
    """<p>The token that identifies the batch of results that you want to see.</p> <p>For example, you submit a ListFeeds request with MaxResults set at 5. The service returns the first batch of results (up to 5) and a NextToken value. To see the next batch of results, you can submit the ListFeeds request a second time and specify the NextToken value. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFeedsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListFeedsRequest:
    out: ListFeedsRequest = {}  # type: ignore[typeddict-item]
    return out
