"""Generated from Smithy shape ``com.amazonaws.storagegateway#DiskIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.disk_id

DiskIds: TypeAlias = list["aws_sdk_storage_gateway.types.disk_id.DiskId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DiskIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DiskIds:
    return list(data)
