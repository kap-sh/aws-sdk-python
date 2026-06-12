"""Generated from Smithy shape ``com.amazonaws.socialmessaging#MetaFlowAssetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.meta_flow_asset

MetaFlowAssetList: TypeAlias = list[
    "aws_sdk_socialmessaging.types.meta_flow_asset.MetaFlowAsset"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetaFlowAssetList) -> list:
    import aws_sdk_socialmessaging.types.meta_flow_asset

    out: list = []
    for item in value:
        out.append(aws_sdk_socialmessaging.types.meta_flow_asset.serialize_json(item))
    return out


def deserialize_json(data: list) -> MetaFlowAssetList:
    import aws_sdk_socialmessaging.types.meta_flow_asset

    out: MetaFlowAssetList = []
    for item in data:
        out.append(aws_sdk_socialmessaging.types.meta_flow_asset.deserialize_json(item))
    return out
