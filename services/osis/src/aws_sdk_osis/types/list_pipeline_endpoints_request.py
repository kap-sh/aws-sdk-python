"""Generated from Smithy shape ``com.amazonaws.osis#ListPipelineEndpointsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_osis.types.max_results
    import aws_sdk_osis.types.next_token


class ListPipelineEndpointsRequest(TypedDict):
    max_results: NotRequired["aws_sdk_osis.types.max_results.MaxResults"]
    """<p>The maximum number of pipeline endpoints to return in the response.</p>"""
    next_token: NotRequired["aws_sdk_osis.types.next_token.NextToken"]
    """<p>If your initial <code>ListPipelineEndpoints</code> operation returns a <code>NextToken</code>, you can include the returned <code>NextToken</code> in subsequent <code>ListPipelineEndpoints</code> operations, which returns results in the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPipelineEndpointsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPipelineEndpointsRequest:
    out: ListPipelineEndpointsRequest = {}  # type: ignore[typeddict-item]
    return out
