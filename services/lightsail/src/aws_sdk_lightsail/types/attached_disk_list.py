"""Generated from Smithy shape ``com.amazonaws.lightsail#AttachedDiskList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.attached_disk

AttachedDiskList: TypeAlias = list["aws_sdk_lightsail.types.attached_disk.AttachedDisk"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttachedDiskList) -> list:
    import aws_sdk_lightsail.types.attached_disk

    out: list = []
    for item in value:
        out.append(aws_sdk_lightsail.types.attached_disk.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AttachedDiskList:
    import aws_sdk_lightsail.types.attached_disk

    out: AttachedDiskList = []
    for item in data:
        out.append(aws_sdk_lightsail.types.attached_disk.deserialize_aws_json_1_1(item))
    return out
