"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ListingSummaryAssociatedEntity``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.product_information


class ListingSummaryAssociatedEntity(TypedDict):
    product: NotRequired[
        "aws_sdk_marketplace_discovery.types.product_information.ProductInformation"
    ]
    """<p>Information about the associated product.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListingSummaryAssociatedEntity) -> dict:
    out: dict = {}
    if "product" in value:
        import aws_sdk_marketplace_discovery.types.product_information

        out["product"] = (
            aws_sdk_marketplace_discovery.types.product_information.serialize_json(
                value["product"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListingSummaryAssociatedEntity:
    out: ListingSummaryAssociatedEntity = {}  # type: ignore[typeddict-item]
    if "product" in data:
        import aws_sdk_marketplace_discovery.types.product_information

        out["product"] = (
            aws_sdk_marketplace_discovery.types.product_information.deserialize_json(
                data["product"]
            )
        )
    return out
