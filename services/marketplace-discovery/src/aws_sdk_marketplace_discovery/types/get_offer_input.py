"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#GetOfferInput``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_marketplace_discovery.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.offer_id

class GetOfferInput(TypedDict):
    offer_id: "aws_sdk_marketplace_discovery.types.offer_id.OfferId"
    """<p>The unique identifier of the offer to retrieve.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: GetOfferInput) -> dict:
    out: dict = {}
    out["offerId"] = value["offer_id"]
    return out


def deserialize_json(data: dict) -> GetOfferInput:
    out: GetOfferInput = {}  # type: ignore[typeddict-item]
    if "offerId" in data:
        out["offer_id"] = data["offerId"]
    else:
        raise DeserializationError("GetOfferInput.offer_id required")
    return out