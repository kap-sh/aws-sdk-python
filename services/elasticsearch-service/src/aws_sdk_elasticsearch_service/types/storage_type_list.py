"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#StorageTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.storage_type

StorageTypeList: TypeAlias = list[
    "aws_sdk_elasticsearch_service.types.storage_type.StorageType"
]


# --- restJson1 ser/de ---
def serialize_json(value: StorageTypeList) -> list:
    import aws_sdk_elasticsearch_service.types.storage_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_elasticsearch_service.types.storage_type.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> StorageTypeList:
    import aws_sdk_elasticsearch_service.types.storage_type

    out: StorageTypeList = []
    for item in data:
        out.append(
            aws_sdk_elasticsearch_service.types.storage_type.deserialize_json(item)
        )
    return out
