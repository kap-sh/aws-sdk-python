"""Generated from Smithy shape ``com.amazonaws.datazone#AssetTargetNames``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_datazone.types.asset_target_name_map

AssetTargetNames: TypeAlias = list["aws_sdk_datazone.types.asset_target_name_map.AssetTargetNameMap"]


# --- restJson1 ser/de ---
def serialize_json(value: AssetTargetNames) -> list:
    import aws_sdk_datazone.types.asset_target_name_map
    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.asset_target_name_map.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssetTargetNames:
    import aws_sdk_datazone.types.asset_target_name_map
    out: AssetTargetNames = []
    for item in data:
        out.append(aws_sdk_datazone.types.asset_target_name_map.deserialize_json(item))
    return out