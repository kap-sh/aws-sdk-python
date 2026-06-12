"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProductViewAggregationValue``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.approximate_count
    import aws_sdk_service_catalog.types.attribute_value


class ProductViewAggregationValue(TypedDict):
    value: NotRequired["aws_sdk_service_catalog.types.attribute_value.AttributeValue"]
    """<p>The value of the product view aggregation.</p>"""
    approximate_count: (
        "aws_sdk_service_catalog.types.approximate_count.ApproximateCount"
    )
    """<p>An approximate count of the products that match the value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProductViewAggregationValue) -> dict:
    out: dict = {}
    if "value" in value:
        out["Value"] = value["value"]
    out["ApproximateCount"] = value.get("approximate_count", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> ProductViewAggregationValue:
    out: ProductViewAggregationValue = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    if "ApproximateCount" in data:
        out["approximate_count"] = data["ApproximateCount"]
    else:
        out["approximate_count"] = 0
    return out
