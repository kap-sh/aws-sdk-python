"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ListVpcEndpointsForDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.domain_name
    import aws_sdk_elasticsearch_service.types.next_token


class ListVpcEndpointsForDomainRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_elasticsearch_service.types.domain_name.DomainName"
    """<p>Name of the ElasticSearch domain whose VPC endpoints are to be listed.</p>"""
    next_token: NotRequired["aws_sdk_elasticsearch_service.types.next_token.NextToken"]
    """<p>Provides an identifier to allow retrieval of paginated results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVpcEndpointsForDomainRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListVpcEndpointsForDomainRequest:
    out: ListVpcEndpointsForDomainRequest = {}  # type: ignore[typeddict-item]
    return out
