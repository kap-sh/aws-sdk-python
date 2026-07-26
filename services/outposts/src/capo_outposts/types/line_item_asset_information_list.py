"""Generated from Smithy shape ``com.amazonaws.outposts#LineItemAssetInformationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_outposts.types.line_item_asset_information

LineItemAssetInformationList: TypeAlias = list[
    "capo_outposts.types.line_item_asset_information.LineItemAssetInformation"
]


# --- restJson1 ser/de ---
def serialize_json(value: LineItemAssetInformationList) -> list:
    import capo_outposts.types.line_item_asset_information

    out: list = []
    for item in value:
        out.append(capo_outposts.types.line_item_asset_information.serialize_json(item))
    return out


def deserialize_json(data: list) -> LineItemAssetInformationList:
    import capo_outposts.types.line_item_asset_information

    out: LineItemAssetInformationList = []
    for item in data:
        out.append(
            capo_outposts.types.line_item_asset_information.deserialize_json(item)
        )
    return out
