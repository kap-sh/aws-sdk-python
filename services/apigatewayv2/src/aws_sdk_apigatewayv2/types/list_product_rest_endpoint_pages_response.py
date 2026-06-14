"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#ListProductRestEndpointPagesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__list_of_product_rest_endpoint_page_summary_no_body
    import aws_sdk_apigatewayv2.types.__string


class ListProductRestEndpointPagesResponse(TypedDict):
    items: NotRequired[
        "aws_sdk_apigatewayv2.types.__list_of_product_rest_endpoint_page_summary_no_body.__listOfProductRestEndpointPageSummaryNoBody"
    ]
    """<p>The elements from this collection.</p>"""
    next_token: NotRequired["aws_sdk_apigatewayv2.types.__string.__string"]
    """<p>The next page of elements from this collection. Not valid for the last element of the collection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProductRestEndpointPagesResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_apigatewayv2.types.__list_of_product_rest_endpoint_page_summary_no_body

        out["items"] = (
            aws_sdk_apigatewayv2.types.__list_of_product_rest_endpoint_page_summary_no_body.serialize_json(
                value["items"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListProductRestEndpointPagesResponse:
    out: ListProductRestEndpointPagesResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_apigatewayv2.types.__list_of_product_rest_endpoint_page_summary_no_body

        out["items"] = (
            aws_sdk_apigatewayv2.types.__list_of_product_rest_endpoint_page_summary_no_body.deserialize_json(
                data["items"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
