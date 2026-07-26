"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ReservedElasticsearchInstanceOfferingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.reserved_elasticsearch_instance_offering

ReservedElasticsearchInstanceOfferingList: TypeAlias = list[
    "capo_elasticsearch_service.types.reserved_elasticsearch_instance_offering.ReservedElasticsearchInstanceOffering"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReservedElasticsearchInstanceOfferingList) -> list:
    import capo_elasticsearch_service.types.reserved_elasticsearch_instance_offering

    out: list = []
    for item in value:
        out.append(
            capo_elasticsearch_service.types.reserved_elasticsearch_instance_offering.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ReservedElasticsearchInstanceOfferingList:
    import capo_elasticsearch_service.types.reserved_elasticsearch_instance_offering

    out: ReservedElasticsearchInstanceOfferingList = []
    for item in data:
        out.append(
            capo_elasticsearch_service.types.reserved_elasticsearch_instance_offering.deserialize_json(
                item
            )
        )
    return out
