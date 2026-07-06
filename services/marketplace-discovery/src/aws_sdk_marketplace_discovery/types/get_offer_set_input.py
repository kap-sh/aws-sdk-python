"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#GetOfferSetInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.offer_set_id


class GetOfferSetInput(TypedDict, closed=True):
    offer_set_id: "aws_sdk_marketplace_discovery.types.offer_set_id.OfferSetId"
    """<p>The unique identifier of the offer set to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOfferSetInput) -> dict:
    out: dict = {}
    out["offerSetId"] = value["offer_set_id"]
    return out


def deserialize_json(data: dict) -> GetOfferSetInput:
    out: GetOfferSetInput = {}  # type: ignore[typeddict-item]
    if "offerSetId" in data:
        out["offer_set_id"] = data["offerSetId"]
    else:
        raise DeserializationError("GetOfferSetInput.offer_set_id required")
    return out
