"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#ProductPageSummaryNoBody``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string_min1_max255
    import aws_sdk_apigatewayv2.types.__string_min10_max30_pattern_az09
    import aws_sdk_apigatewayv2.types.__string_min20_max2048
    import aws_sdk_apigatewayv2.types.__timestamp_iso8601


class ProductPageSummaryNoBody(TypedDict):
    last_modified: NotRequired[
        "aws_sdk_apigatewayv2.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The timestamp when the product page was last modified.</p>"""
    page_title: NotRequired[
        "aws_sdk_apigatewayv2.types.__string_min1_max255.__stringMin1Max255"
    ]
    """<p>The page title.</p>"""
    product_page_arn: NotRequired[
        "aws_sdk_apigatewayv2.types.__string_min20_max2048.__stringMin20Max2048"
    ]
    """<p>The ARN of the product page.</p>"""
    product_page_id: NotRequired[
        "aws_sdk_apigatewayv2.types.__string_min10_max30_pattern_az09.__stringMin10Max30PatternAZ09"
    ]
    """<p>The product page identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProductPageSummaryNoBody) -> dict:
    out: dict = {}
    if "last_modified" in value:
        import aws_sdk_apigatewayv2.types.__timestamp_iso8601

        out["lastModified"] = (
            aws_sdk_apigatewayv2.types.__timestamp_iso8601.serialize_json(
                value["last_modified"]
            )
        )
    if "page_title" in value:
        out["pageTitle"] = value["page_title"]
    if "product_page_arn" in value:
        out["productPageArn"] = value["product_page_arn"]
    if "product_page_id" in value:
        out["productPageId"] = value["product_page_id"]
    return out


def deserialize_json(data: dict) -> ProductPageSummaryNoBody:
    out: ProductPageSummaryNoBody = {}  # type: ignore[typeddict-item]
    if "lastModified" in data:
        import aws_sdk_apigatewayv2.types.__timestamp_iso8601

        out["last_modified"] = (
            aws_sdk_apigatewayv2.types.__timestamp_iso8601.deserialize_json(
                data["lastModified"]
            )
        )
    if "pageTitle" in data:
        out["page_title"] = data["pageTitle"]
    if "productPageArn" in data:
        out["product_page_arn"] = data["productPageArn"]
    if "productPageId" in data:
        out["product_page_id"] = data["productPageId"]
    return out
