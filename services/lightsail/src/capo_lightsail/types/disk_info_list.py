"""Generated from Smithy shape ``com.amazonaws.lightsail#DiskInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.disk_info

DiskInfoList: TypeAlias = list["capo_lightsail.types.disk_info.DiskInfo"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DiskInfoList) -> list:
    import capo_lightsail.types.disk_info

    out: list = []
    for item in value:
        out.append(capo_lightsail.types.disk_info.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DiskInfoList:
    import capo_lightsail.types.disk_info

    out: DiskInfoList = []
    for item in data:
        out.append(capo_lightsail.types.disk_info.deserialize_aws_json_1_1(item))
    return out
