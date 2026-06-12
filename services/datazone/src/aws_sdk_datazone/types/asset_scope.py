"""Generated from Smithy shape ``com.amazonaws.datazone#AssetScope``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_datazone.types.asset_id
    import aws_sdk_datazone.types.filter_ids

class AssetScope(TypedDict):
    asset_id: "aws_sdk_datazone.types.asset_id.AssetId"
    """<p>The asset ID of the asset scope.</p>"""
    filter_ids: "aws_sdk_datazone.types.filter_ids.FilterIds"
    """<p>The filter IDs of the asset scope.</p>"""
    status: "str"
    """<p>The status of the asset scope.</p>"""
    error_message: NotRequired["str"]
    """<p>The error message of the asset scope.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AssetScope) -> dict:
    out: dict = {}
    out["assetId"] = value["asset_id"]
    import aws_sdk_datazone.types.filter_ids
    out["filterIds"] = aws_sdk_datazone.types.filter_ids.serialize_json(value["filter_ids"])
    out["status"] = value["status"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> AssetScope:
    out: AssetScope = {}  # type: ignore[typeddict-item]
    if "assetId" in data:
        out["asset_id"] = data["assetId"]
    else:
        raise DeserializationError("AssetScope.asset_id required")
    if "filterIds" in data:
        import aws_sdk_datazone.types.filter_ids
        out["filter_ids"] = aws_sdk_datazone.types.filter_ids.deserialize_json(data["filterIds"])
    else:
        raise DeserializationError("AssetScope.filter_ids required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("AssetScope.status required")
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out