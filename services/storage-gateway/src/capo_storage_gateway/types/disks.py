"""Generated from Smithy shape ``com.amazonaws.storagegateway#Disks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_storage_gateway.types.disk

Disks: TypeAlias = list["capo_storage_gateway.types.disk.Disk"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Disks) -> list:
    import capo_storage_gateway.types.disk

    out: list = []
    for item in value:
        out.append(capo_storage_gateway.types.disk.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Disks:
    import capo_storage_gateway.types.disk

    out: Disks = []
    for item in data:
        out.append(capo_storage_gateway.types.disk.deserialize_aws_json_1_1(item))
    return out
