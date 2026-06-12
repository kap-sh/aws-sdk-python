"""Generated from Smithy shape ``com.amazonaws.storagegateway#DiskAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.disk_attribute

DiskAttributeList: TypeAlias = list[
    "aws_sdk_storage_gateway.types.disk_attribute.DiskAttribute"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DiskAttributeList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DiskAttributeList:
    return list(data)
