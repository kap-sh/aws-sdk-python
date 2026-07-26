"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#OfferAssociatedEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.offer_set_information
    import capo_marketplace_discovery.types.product_information


class OfferAssociatedEntity(TypedDict, closed=True):
    product: "capo_marketplace_discovery.types.product_information.ProductInformation"
    """<p>Information about the product associated with the offer.</p>"""
    offer_set: NotRequired[
        "capo_marketplace_discovery.types.offer_set_information.OfferSetInformation"
    ]
    """<p>Information about the offer set, if the offer is part of a bundled offer set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OfferAssociatedEntity) -> dict:
    out: dict = {}
    import capo_marketplace_discovery.types.product_information

    out["product"] = (
        capo_marketplace_discovery.types.product_information.serialize_json(
            value["product"]
        )
    )
    if "offer_set" in value:
        import capo_marketplace_discovery.types.offer_set_information

        out["offerSet"] = (
            capo_marketplace_discovery.types.offer_set_information.serialize_json(
                value["offer_set"]
            )
        )
    return out


def deserialize_json(data: dict) -> OfferAssociatedEntity:
    out: OfferAssociatedEntity = {}  # type: ignore[typeddict-item]
    if "product" in data:
        import capo_marketplace_discovery.types.product_information

        out["product"] = (
            capo_marketplace_discovery.types.product_information.deserialize_json(
                data["product"]
            )
        )
    else:
        raise DeserializationError("OfferAssociatedEntity.product required")
    if "offerSet" in data:
        import capo_marketplace_discovery.types.offer_set_information

        out["offer_set"] = (
            capo_marketplace_discovery.types.offer_set_information.deserialize_json(
                data["offerSet"]
            )
        )
    return out
