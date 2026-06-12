"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ElasticsearchInstanceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.es_partition_instance_type

ElasticsearchInstanceTypeList: TypeAlias = list[
    "aws_sdk_elasticsearch_service.types.es_partition_instance_type.ESPartitionInstanceType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ElasticsearchInstanceTypeList) -> list:
    import aws_sdk_elasticsearch_service.types.es_partition_instance_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_elasticsearch_service.types.es_partition_instance_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ElasticsearchInstanceTypeList:
    import aws_sdk_elasticsearch_service.types.es_partition_instance_type

    out: ElasticsearchInstanceTypeList = []
    for item in data:
        out.append(
            aws_sdk_elasticsearch_service.types.es_partition_instance_type.deserialize_json(
                item
            )
        )
    return out
