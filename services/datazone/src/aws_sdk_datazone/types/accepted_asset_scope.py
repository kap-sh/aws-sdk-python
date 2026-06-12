"""Generated from Smithy shape ``com.amazonaws.datazone#AcceptedAssetScope``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_datazone.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_datazone.types.asset_id
    import aws_sdk_datazone.types.filter_ids

class AcceptedAssetScope(TypedDict):
    asset_id: "aws_sdk_datazone.types.asset_id.AssetId"
    """<p>The asset ID of the accepted asset scope.</p>"""
    filter_ids: "aws_sdk_datazone.types.filter_ids.FilterIds"
    """<p>The filter IDs of the accepted asset scope.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AcceptedAssetScope) -> dict:
    out: dict = {}
    out["assetId"] = value["asset_id"]
    import aws_sdk_datazone.types.filter_ids
    out["filterIds"] = aws_sdk_datazone.types.filter_ids.serialize_json(value["filter_ids"])
    return out


def deserialize_json(data: dict) -> AcceptedAssetScope:
    out: AcceptedAssetScope = {}  # type: ignore[typeddict-item]
    if "assetId" in data:
        out["asset_id"] = data["assetId"]
    else:
        raise DeserializationError("AcceptedAssetScope.asset_id required")
    if "filterIds" in data:
        import aws_sdk_datazone.types.filter_ids
        out["filter_ids"] = aws_sdk_datazone.types.filter_ids.deserialize_json(data["filterIds"])
    else:
        raise DeserializationError("AcceptedAssetScope.filter_ids required")
    return out