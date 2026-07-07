"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ListFlowsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.max_results


class ListFlowsRequest(TypedDict, closed=True):
    max_results: NotRequired["aws_sdk_mediaconnect.types.max_results.MaxResults"]
    """<p> The maximum number of results to return per API request. </p> <p>For example, you submit a <code>ListFlows</code> request with MaxResults set at 5. Although 20 items match your request, the service returns no more than the first 5 items. (The service also returns a <code>NextToken</code> value that you can use to fetch the next batch of results.) </p> <p>The service might return fewer results than the <code>MaxResults</code> value. If <code>MaxResults</code> is not included in the request, the service defaults to pagination with a maximum of 10 results per page.</p>"""
    next_token: NotRequired["str"]
    """<p> The token that identifies the batch of results that you want to see. </p> <p>For example, you submit a <code>ListFlows</code> request with MaxResults set at 5. The service returns the first batch of results (up to 5) and a <code>NextToken</code> value. To see the next batch of results, you can submit the <code>ListFlows</code> request a second time and specify the <code>NextToken</code> value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFlowsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListFlowsRequest:
    out: ListFlowsRequest = {}  # type: ignore[typeddict-item]
    return out
