"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#FilterByAssetModel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.boolean
    import capo_iottwinmaker.types.site_wise_external_id
    import capo_iottwinmaker.types.uuid


class FilterByAssetModel(TypedDict, closed=True):
    asset_model_id: NotRequired["capo_iottwinmaker.types.uuid.Uuid"]
    """<p>The asset model Id.</p>"""
    asset_model_external_id: NotRequired[
        "capo_iottwinmaker.types.site_wise_external_id.SiteWiseExternalId"
    ]
    """<p>The external-Id property of an asset model.</p>"""
    include_offspring: NotRequired["capo_iottwinmaker.types.boolean.Boolean"]
    """<p>Include asset offspring. [need desc.]</p>"""
    include_assets: NotRequired["capo_iottwinmaker.types.boolean.Boolean"]
    """<p>Bolean to include assets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterByAssetModel) -> dict:
    out: dict = {}
    if "asset_model_id" in value:
        out["assetModelId"] = value["asset_model_id"]
    if "asset_model_external_id" in value:
        out["assetModelExternalId"] = value["asset_model_external_id"]
    if "include_offspring" in value:
        out["includeOffspring"] = value["include_offspring"]
    if "include_assets" in value:
        out["includeAssets"] = value["include_assets"]
    return out


def deserialize_json(data: dict) -> FilterByAssetModel:
    out: FilterByAssetModel = {}  # type: ignore[typeddict-item]
    if "assetModelId" in data:
        out["asset_model_id"] = data["assetModelId"]
    if "assetModelExternalId" in data:
        out["asset_model_external_id"] = data["assetModelExternalId"]
    if "includeOffspring" in data:
        out["include_offspring"] = data["includeOffspring"]
    if "includeAssets" in data:
        out["include_assets"] = data["includeAssets"]
    return out
