"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#UpdateProductPageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string_min10_max30_pattern_az09
    import aws_sdk_apigatewayv2.types.__string_min20_max2048
    import aws_sdk_apigatewayv2.types.__timestamp_iso8601
    import aws_sdk_apigatewayv2.types.display_content


class UpdateProductPageResponse(TypedDict, closed=True):
    display_content: NotRequired[
        "aws_sdk_apigatewayv2.types.display_content.DisplayContent"
    ]
    """<p>The content of the product page.</p>"""
    last_modified: NotRequired[
        "aws_sdk_apigatewayv2.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The timestamp when the product page was last modified.</p>"""
    product_page_arn: NotRequired[
        "aws_sdk_apigatewayv2.types.__string_min20_max2048.__stringMin20Max2048"
    ]
    """<p>The ARN of the product page.</p>"""
    product_page_id: NotRequired[
        "aws_sdk_apigatewayv2.types.__string_min10_max30_pattern_az09.__stringMin10Max30PatternAZ09"
    ]
    """<p>The product page identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateProductPageResponse) -> dict:
    out: dict = {}
    if "display_content" in value:
        import aws_sdk_apigatewayv2.types.display_content

        out["displayContent"] = (
            aws_sdk_apigatewayv2.types.display_content.serialize_json(
                value["display_content"]
            )
        )
    if "last_modified" in value:
        import aws_sdk_apigatewayv2.types.__timestamp_iso8601

        out["lastModified"] = (
            aws_sdk_apigatewayv2.types.__timestamp_iso8601.serialize_json(
                value["last_modified"]
            )
        )
    if "product_page_arn" in value:
        out["productPageArn"] = value["product_page_arn"]
    if "product_page_id" in value:
        out["productPageId"] = value["product_page_id"]
    return out


def deserialize_json(data: dict) -> UpdateProductPageResponse:
    out: UpdateProductPageResponse = {}  # type: ignore[typeddict-item]
    if "displayContent" in data:
        import aws_sdk_apigatewayv2.types.display_content

        out["display_content"] = (
            aws_sdk_apigatewayv2.types.display_content.deserialize_json(
                data["displayContent"]
            )
        )
    if "lastModified" in data:
        import aws_sdk_apigatewayv2.types.__timestamp_iso8601

        out["last_modified"] = (
            aws_sdk_apigatewayv2.types.__timestamp_iso8601.deserialize_json(
                data["lastModified"]
            )
        )
    if "productPageArn" in data:
        out["product_page_arn"] = data["productPageArn"]
    if "productPageId" in data:
        out["product_page_id"] = data["productPageId"]
    return out
