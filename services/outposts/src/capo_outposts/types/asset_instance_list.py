"""Generated from Smithy shape ``com.amazonaws.outposts#AssetInstanceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_outposts.types.asset_instance

AssetInstanceList: TypeAlias = list["capo_outposts.types.asset_instance.AssetInstance"]


# --- restJson1 ser/de ---
def serialize_json(value: AssetInstanceList) -> list:
    import capo_outposts.types.asset_instance

    out: list = []
    for item in value:
        out.append(capo_outposts.types.asset_instance.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssetInstanceList:
    import capo_outposts.types.asset_instance

    out: AssetInstanceList = []
    for item in data:
        out.append(capo_outposts.types.asset_instance.deserialize_json(item))
    return out
