"""Generated from Smithy shape ``com.amazonaws.datazone#AcceptedAssetScope``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.asset_id
    import capo_datazone.types.filter_ids


class AcceptedAssetScope(TypedDict, closed=True):
    asset_id: "capo_datazone.types.asset_id.AssetId"
    """<p>The asset ID of the accepted asset scope.</p>"""
    filter_ids: "capo_datazone.types.filter_ids.FilterIds"
    """<p>The filter IDs of the accepted asset scope.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AcceptedAssetScope) -> dict:
    out: dict = {}
    out["assetId"] = value["asset_id"]
    import capo_datazone.types.filter_ids

    out["filterIds"] = capo_datazone.types.filter_ids.serialize_json(
        value["filter_ids"]
    )
    return out


def deserialize_json(data: dict) -> AcceptedAssetScope:
    out: AcceptedAssetScope = {}  # type: ignore[typeddict-item]
    if "assetId" in data:
        out["asset_id"] = data["assetId"]
    else:
        raise DeserializationError("AcceptedAssetScope.asset_id required")
    if "filterIds" in data:
        import capo_datazone.types.filter_ids

        out["filter_ids"] = capo_datazone.types.filter_ids.deserialize_json(
            data["filterIds"]
        )
    else:
        raise DeserializationError("AcceptedAssetScope.filter_ids required")
    return out
