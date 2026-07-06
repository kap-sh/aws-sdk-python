"""Generated from Smithy shape ``com.amazonaws.securityhub#DescribeProductsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.next_token
    import aws_sdk_securityhub.types.products_list


class DescribeProductsResponse(TypedDict, closed=True):
    products: NotRequired["aws_sdk_securityhub.types.products_list.ProductsList"]
    """<p>A list of products, including details for each product.</p>"""
    next_token: NotRequired["aws_sdk_securityhub.types.next_token.NextToken"]
    """<p>The pagination token to use to request the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeProductsResponse) -> dict:
    out: dict = {}
    if "products" in value:
        import aws_sdk_securityhub.types.products_list

        out["Products"] = aws_sdk_securityhub.types.products_list.serialize_json(
            value["products"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeProductsResponse:
    out: DescribeProductsResponse = {}  # type: ignore[typeddict-item]
    if "Products" in data:
        import aws_sdk_securityhub.types.products_list

        out["products"] = aws_sdk_securityhub.types.products_list.deserialize_json(
            data["Products"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
