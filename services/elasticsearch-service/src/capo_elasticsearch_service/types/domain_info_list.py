"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DomainInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.domain_info

DomainInfoList: TypeAlias = list[
    "capo_elasticsearch_service.types.domain_info.DomainInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: DomainInfoList) -> list:
    import capo_elasticsearch_service.types.domain_info

    out: list = []
    for item in value:
        out.append(capo_elasticsearch_service.types.domain_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> DomainInfoList:
    import capo_elasticsearch_service.types.domain_info

    out: DomainInfoList = []
    for item in data:
        out.append(capo_elasticsearch_service.types.domain_info.deserialize_json(item))
    return out
