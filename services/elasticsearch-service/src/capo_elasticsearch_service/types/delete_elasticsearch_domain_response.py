"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DeleteElasticsearchDomainResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.elasticsearch_domain_status


class DeleteElasticsearchDomainResponse(TypedDict, closed=True):
    domain_status: NotRequired[
        "capo_elasticsearch_service.types.elasticsearch_domain_status.ElasticsearchDomainStatus"
    ]
    """<p>The status of the Elasticsearch domain being deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteElasticsearchDomainResponse) -> dict:
    out: dict = {}
    if "domain_status" in value:
        import capo_elasticsearch_service.types.elasticsearch_domain_status

        out["DomainStatus"] = (
            capo_elasticsearch_service.types.elasticsearch_domain_status.serialize_json(
                value["domain_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteElasticsearchDomainResponse:
    out: DeleteElasticsearchDomainResponse = {}  # type: ignore[typeddict-item]
    if "DomainStatus" in data:
        import capo_elasticsearch_service.types.elasticsearch_domain_status

        out["domain_status"] = (
            capo_elasticsearch_service.types.elasticsearch_domain_status.deserialize_json(
                data["DomainStatus"]
            )
        )
    return out
