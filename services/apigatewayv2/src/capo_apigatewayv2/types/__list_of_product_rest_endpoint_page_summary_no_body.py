"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#__listOfProductRestEndpointPageSummaryNoBody``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_apigatewayv2.types.product_rest_endpoint_page_summary_no_body

__listOfProductRestEndpointPageSummaryNoBody: TypeAlias = list[
    "capo_apigatewayv2.types.product_rest_endpoint_page_summary_no_body.ProductRestEndpointPageSummaryNoBody"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfProductRestEndpointPageSummaryNoBody) -> list:
    import capo_apigatewayv2.types.product_rest_endpoint_page_summary_no_body

    out: list = []
    for item in value:
        out.append(
            capo_apigatewayv2.types.product_rest_endpoint_page_summary_no_body.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfProductRestEndpointPageSummaryNoBody:
    import capo_apigatewayv2.types.product_rest_endpoint_page_summary_no_body

    out: __listOfProductRestEndpointPageSummaryNoBody = []
    for item in data:
        out.append(
            capo_apigatewayv2.types.product_rest_endpoint_page_summary_no_body.deserialize_json(
                item
            )
        )
    return out
