"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#GetProductInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.product_id


class GetProductInput(TypedDict):
    product_id: "aws_sdk_marketplace_discovery.types.product_id.ProductId"
    """<p>The unique identifier of the product to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProductInput) -> dict:
    out: dict = {}
    out["productId"] = value["product_id"]
    return out


def deserialize_json(data: dict) -> GetProductInput:
    out: GetProductInput = {}  # type: ignore[typeddict-item]
    if "productId" in data:
        out["product_id"] = data["productId"]
    else:
        raise DeserializationError("GetProductInput.product_id required")
    return out
