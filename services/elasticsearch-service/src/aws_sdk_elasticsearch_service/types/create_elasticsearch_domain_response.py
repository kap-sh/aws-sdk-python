"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#CreateElasticsearchDomainResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.elasticsearch_domain_status


class CreateElasticsearchDomainResponse(TypedDict):
    domain_status: NotRequired[
        "aws_sdk_elasticsearch_service.types.elasticsearch_domain_status.ElasticsearchDomainStatus"
    ]
    """<p>The status of the newly created Elasticsearch domain. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateElasticsearchDomainResponse) -> dict:
    out: dict = {}
    if "domain_status" in value:
        import aws_sdk_elasticsearch_service.types.elasticsearch_domain_status

        out["DomainStatus"] = (
            aws_sdk_elasticsearch_service.types.elasticsearch_domain_status.serialize_json(
                value["domain_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateElasticsearchDomainResponse:
    out: CreateElasticsearchDomainResponse = {}  # type: ignore[typeddict-item]
    if "DomainStatus" in data:
        import aws_sdk_elasticsearch_service.types.elasticsearch_domain_status

        out["domain_status"] = (
            aws_sdk_elasticsearch_service.types.elasticsearch_domain_status.deserialize_json(
                data["DomainStatus"]
            )
        )
    return out
