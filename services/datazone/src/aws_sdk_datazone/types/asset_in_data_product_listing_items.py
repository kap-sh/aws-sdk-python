"""Generated from Smithy shape ``com.amazonaws.datazone#AssetInDataProductListingItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.asset_in_data_product_listing_item

AssetInDataProductListingItems: TypeAlias = list[
    "aws_sdk_datazone.types.asset_in_data_product_listing_item.AssetInDataProductListingItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetInDataProductListingItems) -> list:
    import aws_sdk_datazone.types.asset_in_data_product_listing_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_datazone.types.asset_in_data_product_listing_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssetInDataProductListingItems:
    import aws_sdk_datazone.types.asset_in_data_product_listing_item

    out: AssetInDataProductListingItems = []
    for item in data:
        out.append(
            aws_sdk_datazone.types.asset_in_data_product_listing_item.deserialize_json(
                item
            )
        )
    return out
