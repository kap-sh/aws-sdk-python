"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ListBatchEvaluationsRequest``."""

from typing import TypedDict

from typing_extensions import NotRequired


class ListBatchEvaluationsRequest(TypedDict):
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>"""
    next_token: NotRequired["str"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBatchEvaluationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListBatchEvaluationsRequest:
    out: ListBatchEvaluationsRequest = {}  # type: ignore[typeddict-item]
    return out
