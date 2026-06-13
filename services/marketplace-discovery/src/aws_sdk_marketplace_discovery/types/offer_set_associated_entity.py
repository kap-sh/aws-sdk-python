"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#OfferSetAssociatedEntity``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.offer_information
    import aws_sdk_marketplace_discovery.types.product_information


class OfferSetAssociatedEntity(TypedDict):
    product: (
        "aws_sdk_marketplace_discovery.types.product_information.ProductInformation"
    )
    """<p>Information about the product associated with the offer set.</p>"""
    offer: "aws_sdk_marketplace_discovery.types.offer_information.OfferInformation"
    """<p>Information about the offer associated with the offer set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OfferSetAssociatedEntity) -> dict:
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
    return out


def deserialize_json(data: dict) -> OfferSetAssociatedEntity:
    out: OfferSetAssociatedEntity = {}  # type: ignore[typeddict-item]
    if "product" in data:
        import aws_sdk_marketplace_discovery.types.product_information

        out["product"] = (
            aws_sdk_marketplace_discovery.types.product_information.deserialize_json(
                data["product"]
            )
        )
    else:
        raise DeserializationError("OfferSetAssociatedEntity.product required")
    if "offer" in data:
        import aws_sdk_marketplace_discovery.types.offer_information

        out["offer"] = (
            aws_sdk_marketplace_discovery.types.offer_information.deserialize_json(
                data["offer"]
            )
        )
    else:
        raise DeserializationError("OfferSetAssociatedEntity.offer required")
    return out
