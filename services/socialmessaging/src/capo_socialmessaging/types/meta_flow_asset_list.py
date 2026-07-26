"""Generated from Smithy shape ``com.amazonaws.socialmessaging#MetaFlowAssetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_socialmessaging.types.meta_flow_asset

MetaFlowAssetList: TypeAlias = list[
    "capo_socialmessaging.types.meta_flow_asset.MetaFlowAsset"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetaFlowAssetList) -> list:
    import capo_socialmessaging.types.meta_flow_asset

    out: list = []
    for item in value:
        out.append(capo_socialmessaging.types.meta_flow_asset.serialize_json(item))
    return out


def deserialize_json(data: list) -> MetaFlowAssetList:
    import capo_socialmessaging.types.meta_flow_asset

    out: MetaFlowAssetList = []
    for item in data:
        out.append(capo_socialmessaging.types.meta_flow_asset.deserialize_json(item))
    return out
