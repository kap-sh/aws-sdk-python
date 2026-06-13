"""Generated from Smithy shape ``com.amazonaws.datazone#AssetTargetNameMap``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.asset_id


class AssetTargetNameMap(TypedDict):
    asset_id: "aws_sdk_datazone.types.asset_id.AssetId"
    """<p>The identifier of the inventory asset.</p>"""
    target_name: "str"
    """<p>The target name in the asset target name map.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetTargetNameMap) -> dict:
    out: dict = {}
    out["assetId"] = value["asset_id"]
    out["targetName"] = value["target_name"]
    return out


def deserialize_json(data: dict) -> AssetTargetNameMap:
    out: AssetTargetNameMap = {}  # type: ignore[typeddict-item]
    if "assetId" in data:
        out["asset_id"] = data["assetId"]
    else:
        raise DeserializationError("AssetTargetNameMap.asset_id required")
    if "targetName" in data:
        out["target_name"] = data["targetName"]
    else:
        raise DeserializationError("AssetTargetNameMap.target_name required")
    return out
