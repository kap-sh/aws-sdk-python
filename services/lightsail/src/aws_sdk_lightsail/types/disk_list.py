"""Generated from Smithy shape ``com.amazonaws.lightsail#DiskList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.disk

DiskList: TypeAlias = list["aws_sdk_lightsail.types.disk.Disk"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DiskList) -> list:
    import aws_sdk_lightsail.types.disk

    out: list = []
    for item in value:
        out.append(aws_sdk_lightsail.types.disk.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DiskList:
    import aws_sdk_lightsail.types.disk

    out: DiskList = []
    for item in data:
        out.append(aws_sdk_lightsail.types.disk.deserialize_aws_json_1_1(item))
    return out
