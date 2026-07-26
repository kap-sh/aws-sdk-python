"""Generated from Smithy shape ``com.amazonaws.opensearch#ListVpcEndpointsForDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.domain_name
    import capo_opensearch.types.next_token


class ListVpcEndpointsForDomainRequest(TypedDict, closed=True):
    domain_name: "capo_opensearch.types.domain_name.DomainName"
    """<p>The name of the domain to list associated VPC endpoints for.</p>"""
    next_token: NotRequired["capo_opensearch.types.next_token.NextToken"]
    """<p>If your initial <code>ListEndpointsForDomain</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListEndpointsForDomain</code> operations, which returns results in the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVpcEndpointsForDomainRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListVpcEndpointsForDomainRequest:
    out: ListVpcEndpointsForDomainRequest = {}  # type: ignore[typeddict-item]
    return out
