"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ListingAssociatedEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.offer_information
    import capo_marketplace_discovery.types.product_information


class ListingAssociatedEntity(TypedDict, closed=True):
    product: NotRequired[
        "capo_marketplace_discovery.types.product_information.ProductInformation"
    ]
    """<p>Information about the product associated with the listing.</p>"""
    offer: NotRequired[
        "capo_marketplace_discovery.types.offer_information.OfferInformation"
    ]
    """<p>Information about the default offer associated with the listing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListingAssociatedEntity) -> dict:
    out: dict = {}
    if "product" in value:
        import capo_marketplace_discovery.types.product_information

        out["product"] = (
            capo_marketplace_discovery.types.product_information.serialize_json(
                value["product"]
            )
        )
    if "offer" in value:
        import capo_marketplace_discovery.types.offer_information

        out["offer"] = (
            capo_marketplace_discovery.types.offer_information.serialize_json(
                value["offer"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListingAssociatedEntity:
    out: ListingAssociatedEntity = {}  # type: ignore[typeddict-item]
    if "product" in data:
        import capo_marketplace_discovery.types.product_information

        out["product"] = (
            capo_marketplace_discovery.types.product_information.deserialize_json(
                data["product"]
            )
        )
    if "offer" in data:
        import capo_marketplace_discovery.types.offer_information

        out["offer"] = (
            capo_marketplace_discovery.types.offer_information.deserialize_json(
                data["offer"]
            )
        )
    return out
