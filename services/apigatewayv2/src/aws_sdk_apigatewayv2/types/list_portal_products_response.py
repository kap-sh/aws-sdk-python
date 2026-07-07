"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#ListPortalProductsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__list_of_portal_product_summary
    import aws_sdk_apigatewayv2.types.__string_min1_max2048


class ListPortalProductsResponse(TypedDict, closed=True):
    items: NotRequired[
        "aws_sdk_apigatewayv2.types.__list_of_portal_product_summary.__listOfPortalProductSummary"
    ]
    """<p>The elements from this collection.</p>"""
    next_token: NotRequired[
        "aws_sdk_apigatewayv2.types.__string_min1_max2048.__stringMin1Max2048"
    ]
    """<p>The next page of elements from this collection. Not valid for the last element of the collection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPortalProductsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_apigatewayv2.types.__list_of_portal_product_summary

        out["items"] = (
            aws_sdk_apigatewayv2.types.__list_of_portal_product_summary.serialize_json(
                value["items"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPortalProductsResponse:
    out: ListPortalProductsResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_apigatewayv2.types.__list_of_portal_product_summary

        out["items"] = (
            aws_sdk_apigatewayv2.types.__list_of_portal_product_summary.deserialize_json(
                data["items"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
