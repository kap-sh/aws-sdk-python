"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#StorageTypeLimitList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.storage_type_limit

StorageTypeLimitList: TypeAlias = list[
    "aws_sdk_elasticsearch_service.types.storage_type_limit.StorageTypeLimit"
]


# --- restJson1 ser/de ---
def serialize_json(value: StorageTypeLimitList) -> list:
    import aws_sdk_elasticsearch_service.types.storage_type_limit

    out: list = []
    for item in value:
        out.append(
            aws_sdk_elasticsearch_service.types.storage_type_limit.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> StorageTypeLimitList:
    import aws_sdk_elasticsearch_service.types.storage_type_limit

    out: StorageTypeLimitList = []
    for item in data:
        out.append(
            aws_sdk_elasticsearch_service.types.storage_type_limit.deserialize_json(
                item
            )
        )
    return out
