"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ListVpcEndpointsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.next_token


class ListVpcEndpointsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_elasticsearch_service.types.next_token.NextToken"]
    """<p>Identifier to allow retrieval of paginated results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVpcEndpointsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListVpcEndpointsRequest:
    out: ListVpcEndpointsRequest = {}  # type: ignore[typeddict-item]
    return out
