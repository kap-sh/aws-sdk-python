"""Generated from Smithy shape ``com.amazonaws.lightsail#DiskMapList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.disk_map

DiskMapList: TypeAlias = list["capo_lightsail.types.disk_map.DiskMap"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DiskMapList) -> list:
    import capo_lightsail.types.disk_map

    out: list = []
    for item in value:
        out.append(capo_lightsail.types.disk_map.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DiskMapList:
    import capo_lightsail.types.disk_map

    out: DiskMapList = []
    for item in data:
        out.append(capo_lightsail.types.disk_map.deserialize_aws_json_1_1(item))
    return out
