"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#__listOfProductPageSummaryNoBody``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.product_page_summary_no_body

__listOfProductPageSummaryNoBody: TypeAlias = list[
    "aws_sdk_apigatewayv2.types.product_page_summary_no_body.ProductPageSummaryNoBody"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfProductPageSummaryNoBody) -> list:
    import aws_sdk_apigatewayv2.types.product_page_summary_no_body

    out: list = []
    for item in value:
        out.append(
            aws_sdk_apigatewayv2.types.product_page_summary_no_body.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfProductPageSummaryNoBody:
    import aws_sdk_apigatewayv2.types.product_page_summary_no_body

    out: __listOfProductPageSummaryNoBody = []
    for item in data:
        out.append(
            aws_sdk_apigatewayv2.types.product_page_summary_no_body.deserialize_json(
                item
            )
        )
    return out
