"""Generated from Smithy shape ``com.amazonaws.outposts#AssetIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_outposts.types.asset_id

AssetIdList: TypeAlias = list["capo_outposts.types.asset_id.AssetId"]


# --- restJson1 ser/de ---
def serialize_json(value: AssetIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> AssetIdList:
    return list(data)
