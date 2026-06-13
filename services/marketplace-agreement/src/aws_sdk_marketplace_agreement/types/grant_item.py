"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#GrantItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.bounded_string
    import aws_sdk_marketplace_agreement.types.positive_integer_with_default_value_one


class GrantItem(TypedDict):
    dimension_key: NotRequired[
        "aws_sdk_marketplace_agreement.types.bounded_string.BoundedString"
    ]
    """<p>Unique dimension key defined in the product document. Dimensions represent categories of capacity in a product and are specified when the product is listed in AWS Marketplace. </p>"""
    max_quantity: "aws_sdk_marketplace_agreement.types.positive_integer_with_default_value_one.PositiveIntegerWithDefaultValueOne"
    """<p>Maximum amount of capacity that the buyer can be entitled to the given dimension of the product. If <code>MaxQuantity</code> is not provided, the buyer will be able to use an unlimited amount of the given dimension. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GrantItem) -> dict:
    out: dict = {}
    if "dimension_key" in value:
        out["dimensionKey"] = value["dimension_key"]
    out["maxQuantity"] = value.get("max_quantity", 1)
    return out


def deserialize_aws_json_1_0(data: dict) -> GrantItem:
    out: GrantItem = {}  # type: ignore[typeddict-item]
    if "dimensionKey" in data:
        out["dimension_key"] = data["dimensionKey"]
    if "maxQuantity" in data:
        out["max_quantity"] = data["maxQuantity"]
    else:
        out["max_quantity"] = 1
    return out
