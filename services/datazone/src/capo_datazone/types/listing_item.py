"""Generated from Smithy shape ``com.amazonaws.datazone#ListingItem``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_datazone.types.asset_listing
    import capo_datazone.types.data_product_listing


class _ListingItem_assetListing(TypedDict, closed=True):
    assetListing: "capo_datazone.types.asset_listing.AssetListing"


class _ListingItem_dataProductListing(TypedDict, closed=True):
    dataProductListing: "capo_datazone.types.data_product_listing.DataProductListing"


ListingItem: TypeAlias = _ListingItem_assetListing | _ListingItem_dataProductListing


# --- restJson1 ser/de ---
def serialize_json(value: ListingItem) -> dict:
    if "assetListing" in value:
        import capo_datazone.types.asset_listing

        return {
            "assetListing": capo_datazone.types.asset_listing.serialize_json(
                value["assetListing"]
            )
        }
    elif "dataProductListing" in value:
        import capo_datazone.types.data_product_listing

        return {
            "dataProductListing": capo_datazone.types.data_product_listing.serialize_json(
                value["dataProductListing"]
            )
        }
    else:
        raise SerializationError("ListingItem: no variant present")


def deserialize_json(data: dict) -> ListingItem:
    if "assetListing" in data:
        import capo_datazone.types.asset_listing

        return {
            "assetListing": capo_datazone.types.asset_listing.deserialize_json(
                data["assetListing"]
            )
        }
    elif "dataProductListing" in data:
        import capo_datazone.types.data_product_listing

        return {
            "dataProductListing": capo_datazone.types.data_product_listing.deserialize_json(
                data["dataProductListing"]
            )
        }
    else:
        raise DeserializationError("ListingItem: no recognized variant key")
