"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#GetListingInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.listing_id


class GetListingInput(TypedDict, closed=True):
    listing_id: "aws_sdk_marketplace_discovery.types.listing_id.ListingId"
    """<p>The unique identifier of the listing to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetListingInput) -> dict:
    out: dict = {}
    out["listingId"] = value["listing_id"]
    return out


def deserialize_json(data: dict) -> GetListingInput:
    out: GetListingInput = {}  # type: ignore[typeddict-item]
    if "listingId" in data:
        out["listing_id"] = data["listingId"]
    else:
        raise DeserializationError("GetListingInput.listing_id required")
    return out
