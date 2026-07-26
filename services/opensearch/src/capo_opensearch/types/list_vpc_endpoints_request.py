"""Generated from Smithy shape ``com.amazonaws.opensearch#ListVpcEndpointsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.next_token


class ListVpcEndpointsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_opensearch.types.next_token.NextToken"]
    """<p>If your initial <code>ListVpcEndpoints</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListVpcEndpoints</code> operations, which returns results in the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVpcEndpointsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListVpcEndpointsRequest:
    out: ListVpcEndpointsRequest = {}  # type: ignore[typeddict-item]
    return out
