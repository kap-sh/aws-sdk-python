"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ListingAssociatedEntity``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.offer_information
    import aws_sdk_marketplace_discovery.types.product_information


class ListingAssociatedEntity(TypedDict):
    product: NotRequired[
        "aws_sdk_marketplace_discovery.types.product_information.ProductInformation"
    ]
    """<p>Information about the product associated with the listing.</p>"""
    offer: NotRequired[
        "aws_sdk_marketplace_discovery.types.offer_information.OfferInformation"
    ]
    """<p>Information about the default offer associated with the listing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListingAssociatedEntity) -> dict:
    out: dict = {}
    if "product" in value:
        import aws_sdk_marketplace_discovery.types.product_information

        out["product"] = (
            aws_sdk_marketplace_discovery.types.product_information.serialize_json(
                value["product"]
            )
        )
    if "offer" in value:
        import aws_sdk_marketplace_discovery.types.offer_information

        out["offer"] = (
            aws_sdk_marketplace_discovery.types.offer_information.serialize_json(
                value["offer"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListingAssociatedEntity:
    out: ListingAssociatedEntity = {}  # type: ignore[typeddict-item]
    if "product" in data:
        import aws_sdk_marketplace_discovery.types.product_information

        out["product"] = (
            aws_sdk_marketplace_discovery.types.product_information.deserialize_json(
                data["product"]
            )
        )
    if "offer" in data:
        import aws_sdk_marketplace_discovery.types.offer_information

        out["offer"] = (
            aws_sdk_marketplace_discovery.types.offer_information.deserialize_json(
                data["offer"]
            )
        )
    return out
