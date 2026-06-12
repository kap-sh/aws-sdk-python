"""Generated from Smithy shape ``com.amazonaws.outposts#AssetInstanceCapacityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_outposts.types.asset_instance_type_capacity

AssetInstanceCapacityList: TypeAlias = list[
    "aws_sdk_outposts.types.asset_instance_type_capacity.AssetInstanceTypeCapacity"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetInstanceCapacityList) -> list:
    import aws_sdk_outposts.types.asset_instance_type_capacity

    out: list = []
    for item in value:
        out.append(
            aws_sdk_outposts.types.asset_instance_type_capacity.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AssetInstanceCapacityList:
    import aws_sdk_outposts.types.asset_instance_type_capacity

    out: AssetInstanceCapacityList = []
    for item in data:
        out.append(
            aws_sdk_outposts.types.asset_instance_type_capacity.deserialize_json(item)
        )
    return out
