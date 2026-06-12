"""Generated from Smithy shape ``com.amazonaws.outposts#AssetListDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_outposts.types.asset_info

AssetListDefinition: TypeAlias = list["aws_sdk_outposts.types.asset_info.AssetInfo"]


# --- restJson1 ser/de ---
def serialize_json(value: AssetListDefinition) -> list:
    import aws_sdk_outposts.types.asset_info

    out: list = []
    for item in value:
        out.append(aws_sdk_outposts.types.asset_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssetListDefinition:
    import aws_sdk_outposts.types.asset_info

    out: AssetListDefinition = []
    for item in data:
        out.append(aws_sdk_outposts.types.asset_info.deserialize_json(item))
    return out
