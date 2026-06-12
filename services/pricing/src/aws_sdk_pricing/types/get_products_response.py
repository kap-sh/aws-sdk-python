"""Generated from Smithy shape ``com.amazonaws.pricing#GetProductsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pricing.types.format_version
    import aws_sdk_pricing.types.price_list_json_items
    import aws_sdk_pricing.types.string


class GetProductsResponse(TypedDict):
    format_version: NotRequired["aws_sdk_pricing.types.format_version.FormatVersion"]
    """<p>The format version of the response. For example, aws_v1.</p>"""
    price_list: NotRequired[
        "aws_sdk_pricing.types.price_list_json_items.PriceListJsonItems"
    ]
    """<p>The list of products that match your filters. The list contains both the product metadata and the price information.</p>"""
    next_token: NotRequired["aws_sdk_pricing.types.string.String"]
    """<p>The pagination token that indicates the next set of results to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetProductsResponse) -> dict:
    out: dict = {}
    if "format_version" in value:
        out["FormatVersion"] = value["format_version"]
    if "price_list" in value:
        import aws_sdk_pricing.types.price_list_json_items

        out["PriceList"] = (
            aws_sdk_pricing.types.price_list_json_items.serialize_aws_json_1_1(
                value["price_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetProductsResponse:
    out: GetProductsResponse = {}  # type: ignore[typeddict-item]
    if "FormatVersion" in data:
        out["format_version"] = data["FormatVersion"]
    if "PriceList" in data:
        import aws_sdk_pricing.types.price_list_json_items

        out["price_list"] = (
            aws_sdk_pricing.types.price_list_json_items.deserialize_aws_json_1_1(
                data["PriceList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
