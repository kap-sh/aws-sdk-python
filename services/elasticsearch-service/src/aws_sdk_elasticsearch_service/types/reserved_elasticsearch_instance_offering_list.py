"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ReservedElasticsearchInstanceOfferingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.reserved_elasticsearch_instance_offering

ReservedElasticsearchInstanceOfferingList: TypeAlias = list[
    "aws_sdk_elasticsearch_service.types.reserved_elasticsearch_instance_offering.ReservedElasticsearchInstanceOffering"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReservedElasticsearchInstanceOfferingList) -> list:
    import aws_sdk_elasticsearch_service.types.reserved_elasticsearch_instance_offering

    out: list = []
    for item in value:
        out.append(
            aws_sdk_elasticsearch_service.types.reserved_elasticsearch_instance_offering.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ReservedElasticsearchInstanceOfferingList:
    import aws_sdk_elasticsearch_service.types.reserved_elasticsearch_instance_offering

    out: ReservedElasticsearchInstanceOfferingList = []
    for item in data:
        out.append(
            aws_sdk_elasticsearch_service.types.reserved_elasticsearch_instance_offering.deserialize_json(
                item
            )
        )
    return out
