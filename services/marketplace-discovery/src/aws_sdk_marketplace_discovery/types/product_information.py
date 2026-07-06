"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ProductInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.non_empty_string
    import aws_sdk_marketplace_discovery.types.product_id
    import aws_sdk_marketplace_discovery.types.seller_information


class ProductInformation(TypedDict, closed=True):
    product_id: "aws_sdk_marketplace_discovery.types.product_id.ProductId"
    """<p>The unique identifier of the product.</p>"""
    product_name: "aws_sdk_marketplace_discovery.types.non_empty_string.NonEmptyString"
    """<p>The human-readable display name of the product.</p>"""
    manufacturer: (
        "aws_sdk_marketplace_discovery.types.seller_information.SellerInformation"
    )
    """<p>The entity who manufactured the product.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProductInformation) -> dict:
    out: dict = {}
    out["productId"] = value["product_id"]
    out["productName"] = value["product_name"]
    import aws_sdk_marketplace_discovery.types.seller_information

    out["manufacturer"] = (
        aws_sdk_marketplace_discovery.types.seller_information.serialize_json(
            value["manufacturer"]
        )
    )
    return out


def deserialize_json(data: dict) -> ProductInformation:
    out: ProductInformation = {}  # type: ignore[typeddict-item]
    if "productId" in data:
        out["product_id"] = data["productId"]
    else:
        raise DeserializationError("ProductInformation.product_id required")
    if "productName" in data:
        out["product_name"] = data["productName"]
    else:
        raise DeserializationError("ProductInformation.product_name required")
    if "manufacturer" in data:
        import aws_sdk_marketplace_discovery.types.seller_information

        out["manufacturer"] = (
            aws_sdk_marketplace_discovery.types.seller_information.deserialize_json(
                data["manufacturer"]
            )
        )
    else:
        raise DeserializationError("ProductInformation.manufacturer required")
    return out
