"""Generated from Smithy shape ``com.amazonaws.opensearch#ListVpcEndpointAccessRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.domain_name
    import aws_sdk_opensearch.types.next_token


class ListVpcEndpointAccessRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_opensearch.types.domain_name.DomainName"
    """<p>The name of the OpenSearch Service domain to retrieve access information for.</p>"""
    next_token: NotRequired["aws_sdk_opensearch.types.next_token.NextToken"]
    """<p>If your initial <code>ListVpcEndpointAccess</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListVpcEndpointAccess</code> operations, which returns results in the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVpcEndpointAccessRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListVpcEndpointAccessRequest:
    out: ListVpcEndpointAccessRequest = {}  # type: ignore[typeddict-item]
    return out
