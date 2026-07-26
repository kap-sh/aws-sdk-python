"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DescribeElasticsearchDomainConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.domain_name


class DescribeElasticsearchDomainConfigRequest(TypedDict, closed=True):
    domain_name: "capo_elasticsearch_service.types.domain_name.DomainName"
    """<p>The Elasticsearch domain that you want to get information about.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeElasticsearchDomainConfigRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeElasticsearchDomainConfigRequest:
    out: DescribeElasticsearchDomainConfigRequest = {}  # type: ignore[typeddict-item]
    return out
