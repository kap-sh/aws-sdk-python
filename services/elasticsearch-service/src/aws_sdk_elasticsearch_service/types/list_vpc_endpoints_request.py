"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ListVpcEndpointsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.next_token


class ListVpcEndpointsRequest(TypedDict):
    next_token: NotRequired["aws_sdk_elasticsearch_service.types.next_token.NextToken"]
    """<p>Identifier to allow retrieval of paginated results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVpcEndpointsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListVpcEndpointsRequest:
    out: ListVpcEndpointsRequest = {}  # type: ignore[typeddict-item]
    return out
