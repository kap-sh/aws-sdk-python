"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DescribeElasticsearchDomainRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.domain_name


class DescribeElasticsearchDomainRequest(TypedDict):
    domain_name: "aws_sdk_elasticsearch_service.types.domain_name.DomainName"
    """<p>The name of the Elasticsearch domain for which you want information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeElasticsearchDomainRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeElasticsearchDomainRequest:
    out: DescribeElasticsearchDomainRequest = {}  # type: ignore[typeddict-item]
    return out
