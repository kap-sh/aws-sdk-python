"""Generated from Smithy shape ``com.amazonaws.outposts#AssetTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_outposts.types.asset_type

AssetTypeList: TypeAlias = list["aws_sdk_outposts.types.asset_type.AssetType"]


# --- restJson1 ser/de ---
def serialize_json(value: AssetTypeList) -> list:
    import aws_sdk_outposts.types.asset_type

    out: list = []
    for item in value:
        out.append(aws_sdk_outposts.types.asset_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssetTypeList:
    import aws_sdk_outposts.types.asset_type

    out: AssetTypeList = []
    for item in data:
        out.append(aws_sdk_outposts.types.asset_type.deserialize_json(item))
    return out
