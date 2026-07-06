"""Generated from Smithy shape ``com.amazonaws.datazone#AssetListingDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.listing_id
    import aws_sdk_datazone.types.listing_status


class AssetListingDetails(TypedDict, closed=True):
    listing_id: "aws_sdk_datazone.types.listing_id.ListingId"
    """<p>The identifier of an asset published in an Amazon DataZone catalog. </p>"""
    listing_status: "aws_sdk_datazone.types.listing_status.ListingStatus"
    """<p>The status of an asset published in an Amazon DataZone catalog. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetListingDetails) -> dict:
    out: dict = {}
    out["listingId"] = value["listing_id"]
    import aws_sdk_datazone.types.listing_status

    out["listingStatus"] = aws_sdk_datazone.types.listing_status.serialize_json(
        value["listing_status"]
    )
    return out


def deserialize_json(data: dict) -> AssetListingDetails:
    out: AssetListingDetails = {}  # type: ignore[typeddict-item]
    if "listingId" in data:
        out["listing_id"] = data["listingId"]
    else:
        raise DeserializationError("AssetListingDetails.listing_id required")
    if "listingStatus" in data:
        import aws_sdk_datazone.types.listing_status

        out["listing_status"] = aws_sdk_datazone.types.listing_status.deserialize_json(
            data["listingStatus"]
        )
    else:
        raise DeserializationError("AssetListingDetails.listing_status required")
    return out
