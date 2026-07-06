"""Generated from Smithy shape ``com.amazonaws.osis#ListPipelinesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_osis.types.max_results
    import aws_sdk_osis.types.next_token


class ListPipelinesRequest(TypedDict, closed=True):
    max_results: NotRequired["aws_sdk_osis.types.max_results.MaxResults"]
    """<p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.</p>"""
    next_token: NotRequired["aws_sdk_osis.types.next_token.NextToken"]
    """<p>If your initial <code>ListPipelines</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListPipelines</code> operations, which returns results in the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPipelinesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPipelinesRequest:
    out: ListPipelinesRequest = {}  # type: ignore[typeddict-item]
    return out
