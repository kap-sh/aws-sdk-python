"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ElasticsearchVersionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.elasticsearch_version_string

ElasticsearchVersionList: TypeAlias = list[
    "capo_elasticsearch_service.types.elasticsearch_version_string.ElasticsearchVersionString"
]


# --- restJson1 ser/de ---
def serialize_json(value: ElasticsearchVersionList) -> list:
    return list(value)


def deserialize_json(data: list) -> ElasticsearchVersionList:
    return list(data)
