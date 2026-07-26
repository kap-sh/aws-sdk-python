"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#OfferSetAssociatedEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.offer_information
    import capo_marketplace_discovery.types.product_information


class OfferSetAssociatedEntity(TypedDict, closed=True):
    product: "capo_marketplace_discovery.types.product_information.ProductInformation"
    """<p>Information about the product associated with the offer set.</p>"""
    offer: "capo_marketplace_discovery.types.offer_information.OfferInformation"
    """<p>Information about the offer associated with the offer set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OfferSetAssociatedEntity) -> dict:
    out: dict = {}
    import capo_marketplace_discovery.types.product_information

    out["product"] = (
        capo_marketplace_discovery.types.product_information.serialize_json(
            value["product"]
        )
    )
    import capo_marketplace_discovery.types.offer_information

    out["offer"] = capo_marketplace_discovery.types.offer_information.serialize_json(
        value["offer"]
    )
    return out


def deserialize_json(data: dict) -> OfferSetAssociatedEntity:
    out: OfferSetAssociatedEntity = {}  # type: ignore[typeddict-item]
    if "product" in data:
        import capo_marketplace_discovery.types.product_information

        out["product"] = (
            capo_marketplace_discovery.types.product_information.deserialize_json(
                data["product"]
            )
        )
    else:
        raise DeserializationError("OfferSetAssociatedEntity.product required")
    if "offer" in data:
        import capo_marketplace_discovery.types.offer_information

        out["offer"] = (
            capo_marketplace_discovery.types.offer_information.deserialize_json(
                data["offer"]
            )
        )
    else:
        raise DeserializationError("OfferSetAssociatedEntity.offer required")
    return out
