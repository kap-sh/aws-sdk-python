"""Generated from Smithy shape ``com.amazonaws.socialmessaging#MetaFlowAsset``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_socialmessaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.meta_flow_asset_download_url
    import aws_sdk_socialmessaging.types.meta_flow_asset_name
    import aws_sdk_socialmessaging.types.meta_flow_asset_type


class MetaFlowAsset(TypedDict):
    name: "aws_sdk_socialmessaging.types.meta_flow_asset_name.MetaFlowAssetName"
    """<p>The filename of the asset (for example, flow.json).</p>"""
    asset_type: "aws_sdk_socialmessaging.types.meta_flow_asset_type.MetaFlowAssetType"
    """<p>The type of asset. Currently the only supported value is FLOW_JSON.</p>"""
    download_url: "aws_sdk_socialmessaging.types.meta_flow_asset_download_url.MetaFlowAssetDownloadUrl"
    """<p>A presigned URL from Meta for downloading the asset. The URL expires after a short period.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetaFlowAsset) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["assetType"] = value["asset_type"]
    out["downloadUrl"] = value["download_url"]
    return out


def deserialize_json(data: dict) -> MetaFlowAsset:
    out: MetaFlowAsset = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("MetaFlowAsset.name required")
    if "assetType" in data:
        out["asset_type"] = data["assetType"]
    else:
        raise DeserializationError("MetaFlowAsset.asset_type required")
    if "downloadUrl" in data:
        out["download_url"] = data["downloadUrl"]
    else:
        raise DeserializationError("MetaFlowAsset.download_url required")
    return out
