"""Generated from Smithy shape ``com.amazonaws.securityhub#DescribeProductsV2Response``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.next_token
    import capo_securityhub.types.products_v2_list


class DescribeProductsV2Response(TypedDict, closed=True):
    products_v2: NotRequired["capo_securityhub.types.products_v2_list.ProductsV2List"]
    """<p>Gets information about the product integration.</p>"""
    next_token: NotRequired["capo_securityhub.types.next_token.NextToken"]
    """<p>The pagination token to use to request the next page of results. Otherwise, this parameter is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeProductsV2Response) -> dict:
    out: dict = {}
    if "products_v2" in value:
        import capo_securityhub.types.products_v2_list

        out["ProductsV2"] = capo_securityhub.types.products_v2_list.serialize_json(
            value["products_v2"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeProductsV2Response:
    out: DescribeProductsV2Response = {}  # type: ignore[typeddict-item]
    if "ProductsV2" in data:
        import capo_securityhub.types.products_v2_list

        out["products_v2"] = capo_securityhub.types.products_v2_list.deserialize_json(
            data["ProductsV2"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
