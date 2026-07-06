"""Generated from Smithy shape ``com.amazonaws.eks#MarketplaceInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.string


class MarketplaceInformation(TypedDict, closed=True):
    product_id: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The product ID from the Amazon Web Services Marketplace.</p>"""
    product_url: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The product URL from the Amazon Web Services Marketplace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MarketplaceInformation) -> dict:
    out: dict = {}
    if "product_id" in value:
        out["productId"] = value["product_id"]
    if "product_url" in value:
        out["productUrl"] = value["product_url"]
    return out


def deserialize_json(data: dict) -> MarketplaceInformation:
    out: MarketplaceInformation = {}  # type: ignore[typeddict-item]
    if "productId" in data:
        out["product_id"] = data["productId"]
    if "productUrl" in data:
        out["product_url"] = data["productUrl"]
    return out
