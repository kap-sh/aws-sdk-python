"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#PurchaseOptionAssociatedEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.offer_information
    import aws_sdk_marketplace_discovery.types.offer_set_information
    import aws_sdk_marketplace_discovery.types.product_information


class PurchaseOptionAssociatedEntity(TypedDict, closed=True):
    product: (
        "aws_sdk_marketplace_discovery.types.product_information.ProductInformation"
    )
    """<p>Information about the product associated with the purchase option.</p>"""
    offer: "aws_sdk_marketplace_discovery.types.offer_information.OfferInformation"
    """<p>Information about the offer associated with the purchase option.</p>"""
    offer_set: NotRequired[
        "aws_sdk_marketplace_discovery.types.offer_set_information.OfferSetInformation"
    ]
    """<p>Information about the offer set, if the purchase option is part of a bundled offer set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PurchaseOptionAssociatedEntity) -> dict:
    out: dict = {}
    import aws_sdk_marketplace_discovery.types.product_information

    out["product"] = (
        aws_sdk_marketplace_discovery.types.product_information.serialize_json(
            value["product"]
        )
    )
    import aws_sdk_marketplace_discovery.types.offer_information

    out["offer"] = aws_sdk_marketplace_discovery.types.offer_information.serialize_json(
        value["offer"]
    )
    if "offer_set" in value:
        import aws_sdk_marketplace_discovery.types.offer_set_information

        out["offerSet"] = (
            aws_sdk_marketplace_discovery.types.offer_set_information.serialize_json(
                value["offer_set"]
            )
        )
    return out


def deserialize_json(data: dict) -> PurchaseOptionAssociatedEntity:
    out: PurchaseOptionAssociatedEntity = {}  # type: ignore[typeddict-item]
    if "product" in data:
        import aws_sdk_marketplace_discovery.types.product_information

        out["product"] = (
            aws_sdk_marketplace_discovery.types.product_information.deserialize_json(
                data["product"]
            )
        )
    else:
        raise DeserializationError("PurchaseOptionAssociatedEntity.product required")
    if "offer" in data:
        import aws_sdk_marketplace_discovery.types.offer_information

        out["offer"] = (
            aws_sdk_marketplace_discovery.types.offer_information.deserialize_json(
                data["offer"]
            )
        )
    else:
        raise DeserializationError("PurchaseOptionAssociatedEntity.offer required")
    if "offerSet" in data:
        import aws_sdk_marketplace_discovery.types.offer_set_information

        out["offer_set"] = (
            aws_sdk_marketplace_discovery.types.offer_set_information.deserialize_json(
                data["offerSet"]
            )
        )
    return out
