"""Generated from Smithy shape ``com.amazonaws.datazone#SubscribedListingItem``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.subscribed_asset_listing
    import aws_sdk_datazone.types.subscribed_product_listing


class _SubscribedListingItem_assetListing(TypedDict):
    assetListing: (
        "aws_sdk_datazone.types.subscribed_asset_listing.SubscribedAssetListing"
    )


class _SubscribedListingItem_productListing(TypedDict):
    productListing: (
        "aws_sdk_datazone.types.subscribed_product_listing.SubscribedProductListing"
    )


SubscribedListingItem: TypeAlias = (
    _SubscribedListingItem_assetListing | _SubscribedListingItem_productListing
)


# --- restJson1 ser/de ---
def serialize_json(value: SubscribedListingItem) -> dict:
    if "assetListing" in value:
        import aws_sdk_datazone.types.subscribed_asset_listing

        return {
            "assetListing": aws_sdk_datazone.types.subscribed_asset_listing.serialize_json(
                value["assetListing"]
            )
        }
    elif "productListing" in value:
        import aws_sdk_datazone.types.subscribed_product_listing

        return {
            "productListing": aws_sdk_datazone.types.subscribed_product_listing.serialize_json(
                value["productListing"]
            )
        }
    else:
        raise SerializationError("SubscribedListingItem: no variant present")


def deserialize_json(data: dict) -> SubscribedListingItem:
    if "assetListing" in data:
        import aws_sdk_datazone.types.subscribed_asset_listing

        return {
            "assetListing": aws_sdk_datazone.types.subscribed_asset_listing.deserialize_json(
                data["assetListing"]
            )
        }
    elif "productListing" in data:
        import aws_sdk_datazone.types.subscribed_product_listing

        return {
            "productListing": aws_sdk_datazone.types.subscribed_product_listing.deserialize_json(
                data["productListing"]
            )
        }
    else:
        raise DeserializationError("SubscribedListingItem: no recognized variant key")
