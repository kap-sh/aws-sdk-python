"""Generated from Smithy shape ``com.amazonaws.datazone#SearchResultItem``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.asset_listing_item
    import aws_sdk_datazone.types.data_product_listing_item


class _SearchResultItem_assetListing(TypedDict, closed=True):
    assetListing: "aws_sdk_datazone.types.asset_listing_item.AssetListingItem"


class _SearchResultItem_dataProductListing(TypedDict, closed=True):
    dataProductListing: (
        "aws_sdk_datazone.types.data_product_listing_item.DataProductListingItem"
    )


SearchResultItem: TypeAlias = (
    _SearchResultItem_assetListing | _SearchResultItem_dataProductListing
)


# --- restJson1 ser/de ---
def serialize_json(value: SearchResultItem) -> dict:
    if "assetListing" in value:
        import aws_sdk_datazone.types.asset_listing_item

        return {
            "assetListing": aws_sdk_datazone.types.asset_listing_item.serialize_json(
                value["assetListing"]
            )
        }
    elif "dataProductListing" in value:
        import aws_sdk_datazone.types.data_product_listing_item

        return {
            "dataProductListing": aws_sdk_datazone.types.data_product_listing_item.serialize_json(
                value["dataProductListing"]
            )
        }
    else:
        raise SerializationError("SearchResultItem: no variant present")


def deserialize_json(data: dict) -> SearchResultItem:
    if "assetListing" in data:
        import aws_sdk_datazone.types.asset_listing_item

        return {
            "assetListing": aws_sdk_datazone.types.asset_listing_item.deserialize_json(
                data["assetListing"]
            )
        }
    elif "dataProductListing" in data:
        import aws_sdk_datazone.types.data_product_listing_item

        return {
            "dataProductListing": aws_sdk_datazone.types.data_product_listing_item.deserialize_json(
                data["dataProductListing"]
            )
        }
    else:
        raise DeserializationError("SearchResultItem: no recognized variant key")
