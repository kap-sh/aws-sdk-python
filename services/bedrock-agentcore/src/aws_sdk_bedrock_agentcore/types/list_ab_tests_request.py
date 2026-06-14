"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ListABTestsRequest``."""

from typing import TypedDict

from typing_extensions import NotRequired


class ListABTestsRequest(TypedDict):
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>"""
    next_token: NotRequired["str"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListABTestsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListABTestsRequest:
    out: ListABTestsRequest = {}  # type: ignore[typeddict-item]
    return out
