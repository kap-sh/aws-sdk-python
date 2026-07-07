"""Generated from Smithy shape ``com.amazonaws.osis#ListPipelineEndpointConnectionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_osis.types.max_results
    import aws_sdk_osis.types.next_token


class ListPipelineEndpointConnectionsRequest(TypedDict, closed=True):
    max_results: NotRequired["aws_sdk_osis.types.max_results.MaxResults"]
    """<p>The maximum number of pipeline endpoint connections to return in the response.</p>"""
    next_token: NotRequired["aws_sdk_osis.types.next_token.NextToken"]
    """<p>If your initial <code>ListPipelineEndpointConnections</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListPipelineEndpointConnections</code> operations, which returns results in the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPipelineEndpointConnectionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPipelineEndpointConnectionsRequest:
    out: ListPipelineEndpointConnectionsRequest = {}  # type: ignore[typeddict-item]
    return out
