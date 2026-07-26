"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ElasticsearchDomainStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.elasticsearch_domain_status

ElasticsearchDomainStatusList: TypeAlias = list[
    "capo_elasticsearch_service.types.elasticsearch_domain_status.ElasticsearchDomainStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: ElasticsearchDomainStatusList) -> list:
    import capo_elasticsearch_service.types.elasticsearch_domain_status

    out: list = []
    for item in value:
        out.append(
            capo_elasticsearch_service.types.elasticsearch_domain_status.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ElasticsearchDomainStatusList:
    import capo_elasticsearch_service.types.elasticsearch_domain_status

    out: ElasticsearchDomainStatusList = []
    for item in data:
        out.append(
            capo_elasticsearch_service.types.elasticsearch_domain_status.deserialize_json(
                item
            )
        )
    return out
