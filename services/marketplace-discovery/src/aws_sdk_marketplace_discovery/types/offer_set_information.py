"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#OfferSetInformation``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.offer_set_id
    import aws_sdk_marketplace_discovery.types.seller_information


class OfferSetInformation(TypedDict):
    offer_set_id: "aws_sdk_marketplace_discovery.types.offer_set_id.OfferSetId"
    """<p>The unique identifier of the offer set.</p>"""
    seller_of_record: (
        "aws_sdk_marketplace_discovery.types.seller_information.SellerInformation"
    )
    """<p>The entity responsible for selling the products under this offer set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OfferSetInformation) -> dict:
    out: dict = {}
    out["offerSetId"] = value["offer_set_id"]
    import aws_sdk_marketplace_discovery.types.seller_information

    out["sellerOfRecord"] = (
        aws_sdk_marketplace_discovery.types.seller_information.serialize_json(
            value["seller_of_record"]
        )
    )
    return out


def deserialize_json(data: dict) -> OfferSetInformation:
    out: OfferSetInformation = {}  # type: ignore[typeddict-item]
    if "offerSetId" in data:
        out["offer_set_id"] = data["offerSetId"]
    else:
        raise DeserializationError("OfferSetInformation.offer_set_id required")
    if "sellerOfRecord" in data:
        import aws_sdk_marketplace_discovery.types.seller_information

        out["seller_of_record"] = (
            aws_sdk_marketplace_discovery.types.seller_information.deserialize_json(
                data["sellerOfRecord"]
            )
        )
    else:
        raise DeserializationError("OfferSetInformation.seller_of_record required")
    return out
