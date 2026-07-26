"""Generated from Smithy shape ``com.amazonaws.outposts#LineItemAssetInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.asset_id
    import capo_outposts.types.mac_address_list


class LineItemAssetInformation(TypedDict, closed=True):
    asset_id: NotRequired["capo_outposts.types.asset_id.AssetId"]
    """<p> The ID of the asset. An Outpost asset can be a single server within an Outposts rack or an Outposts server configuration.</p>"""
    mac_address_list: NotRequired["capo_outposts.types.mac_address_list.MacAddressList"]
    """<p> The MAC addresses of the asset. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LineItemAssetInformation) -> dict:
    out: dict = {}
    if "asset_id" in value:
        out["AssetId"] = value["asset_id"]
    if "mac_address_list" in value:
        import capo_outposts.types.mac_address_list

        out["MacAddressList"] = capo_outposts.types.mac_address_list.serialize_json(
            value["mac_address_list"]
        )
    return out


def deserialize_json(data: dict) -> LineItemAssetInformation:
    out: LineItemAssetInformation = {}  # type: ignore[typeddict-item]
    if "AssetId" in data:
        out["asset_id"] = data["AssetId"]
    if "MacAddressList" in data:
        import capo_outposts.types.mac_address_list

        out["mac_address_list"] = capo_outposts.types.mac_address_list.deserialize_json(
            data["MacAddressList"]
        )
    return out
