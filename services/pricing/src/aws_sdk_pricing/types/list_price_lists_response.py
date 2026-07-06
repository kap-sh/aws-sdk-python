"""Generated from Smithy shape ``com.amazonaws.pricing#ListPriceListsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pricing.types.price_lists
    import aws_sdk_pricing.types.string


class ListPriceListsResponse(TypedDict, closed=True):
    price_lists: NotRequired["aws_sdk_pricing.types.price_lists.PriceLists"]
    """<p>The type of price list references that match your request. </p>"""
    next_token: NotRequired["aws_sdk_pricing.types.string.String"]
    """<p>The pagination token that indicates the next set of results to retrieve. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPriceListsResponse) -> dict:
    out: dict = {}
    if "price_lists" in value:
        import aws_sdk_pricing.types.price_lists

        out["PriceLists"] = aws_sdk_pricing.types.price_lists.serialize_aws_json_1_1(
            value["price_lists"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPriceListsResponse:
    out: ListPriceListsResponse = {}  # type: ignore[typeddict-item]
    if "PriceLists" in data:
        import aws_sdk_pricing.types.price_lists

        out["price_lists"] = aws_sdk_pricing.types.price_lists.deserialize_aws_json_1_1(
            data["PriceLists"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
