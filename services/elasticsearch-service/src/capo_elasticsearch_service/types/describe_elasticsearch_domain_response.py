"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DescribeElasticsearchDomainResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_elasticsearch_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.elasticsearch_domain_status


class DescribeElasticsearchDomainResponse(TypedDict, closed=True):
    domain_status: "capo_elasticsearch_service.types.elasticsearch_domain_status.ElasticsearchDomainStatus"
    """<p>The current status of the Elasticsearch domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeElasticsearchDomainResponse) -> dict:
    out: dict = {}
    import capo_elasticsearch_service.types.elasticsearch_domain_status

    out["DomainStatus"] = (
        capo_elasticsearch_service.types.elasticsearch_domain_status.serialize_json(
            value["domain_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> DescribeElasticsearchDomainResponse:
    out: DescribeElasticsearchDomainResponse = {}  # type: ignore[typeddict-item]
    if "DomainStatus" in data:
        import capo_elasticsearch_service.types.elasticsearch_domain_status

        out["domain_status"] = (
            capo_elasticsearch_service.types.elasticsearch_domain_status.deserialize_json(
                data["DomainStatus"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeElasticsearchDomainResponse.domain_status required"
        )
    return out
