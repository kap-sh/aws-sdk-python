"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetHierarchyInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.id


class AssetHierarchyInfo(TypedDict, closed=True):
    parent_asset_id: NotRequired["capo_iotsitewise.types.id.ID"]
    """<p>The ID of the parent asset in this asset relationship.</p>"""
    child_asset_id: NotRequired["capo_iotsitewise.types.id.ID"]
    """<p>The ID of the child asset in this asset relationship.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetHierarchyInfo) -> dict:
    out: dict = {}
    if "parent_asset_id" in value:
        out["parentAssetId"] = value["parent_asset_id"]
    if "child_asset_id" in value:
        out["childAssetId"] = value["child_asset_id"]
    return out


def deserialize_json(data: dict) -> AssetHierarchyInfo:
    out: AssetHierarchyInfo = {}  # type: ignore[typeddict-item]
    if "parentAssetId" in data:
        out["parent_asset_id"] = data["parentAssetId"]
    if "childAssetId" in data:
        out["child_asset_id"] = data["childAssetId"]
    return out
