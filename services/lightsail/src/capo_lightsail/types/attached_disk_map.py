"""Generated from Smithy shape ``com.amazonaws.lightsail#AttachedDiskMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.disk_map_list
    import capo_lightsail.types.resource_name

AttachedDiskMap: TypeAlias = dict[
    "capo_lightsail.types.resource_name.ResourceName",
    "capo_lightsail.types.disk_map_list.DiskMapList",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: AttachedDiskMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_lightsail.types.disk_map_list

        out[key] = capo_lightsail.types.disk_map_list.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> AttachedDiskMap:
    out: AttachedDiskMap = {}
    for key, value in data.items():
        import capo_lightsail.types.disk_map_list

        out[key] = capo_lightsail.types.disk_map_list.deserialize_aws_json_1_1(value)
    return out
