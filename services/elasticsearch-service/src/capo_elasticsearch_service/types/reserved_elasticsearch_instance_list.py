"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ReservedElasticsearchInstanceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.reserved_elasticsearch_instance

ReservedElasticsearchInstanceList: TypeAlias = list[
    "capo_elasticsearch_service.types.reserved_elasticsearch_instance.ReservedElasticsearchInstance"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReservedElasticsearchInstanceList) -> list:
    import capo_elasticsearch_service.types.reserved_elasticsearch_instance

    out: list = []
    for item in value:
        out.append(
            capo_elasticsearch_service.types.reserved_elasticsearch_instance.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ReservedElasticsearchInstanceList:
    import capo_elasticsearch_service.types.reserved_elasticsearch_instance

    out: ReservedElasticsearchInstanceList = []
    for item in data:
        out.append(
            capo_elasticsearch_service.types.reserved_elasticsearch_instance.deserialize_json(
                item
            )
        )
    return out
