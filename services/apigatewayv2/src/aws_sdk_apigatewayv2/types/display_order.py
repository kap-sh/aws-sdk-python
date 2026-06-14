"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#DisplayOrder``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__list_of__string_min20_max2048
    import aws_sdk_apigatewayv2.types.__list_of_section
    import aws_sdk_apigatewayv2.types.__string_min20_max2048


class DisplayOrder(TypedDict):
    contents: NotRequired[
        "aws_sdk_apigatewayv2.types.__list_of_section.__listOfSection"
    ]
    """<p>Represents a list of sections which include section name and list of product REST endpoints for a product.</p>"""
    overview_page_arn: NotRequired[
        "aws_sdk_apigatewayv2.types.__string_min20_max2048.__stringMin20Max2048"
    ]
    """<p>The ARN of the overview page.</p>"""
    product_page_arns: NotRequired[
        "aws_sdk_apigatewayv2.types.__list_of__string_min20_max2048.__listOf__stringMin20Max2048"
    ]
    """<p>The product page ARNs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisplayOrder) -> dict:
    out: dict = {}
    if "contents" in value:
        import aws_sdk_apigatewayv2.types.__list_of_section

        out["contents"] = aws_sdk_apigatewayv2.types.__list_of_section.serialize_json(
            value["contents"]
        )
    if "overview_page_arn" in value:
        out["overviewPageArn"] = value["overview_page_arn"]
    if "product_page_arns" in value:
        import aws_sdk_apigatewayv2.types.__list_of__string_min20_max2048

        out["productPageArns"] = (
            aws_sdk_apigatewayv2.types.__list_of__string_min20_max2048.serialize_json(
                value["product_page_arns"]
            )
        )
    return out


def deserialize_json(data: dict) -> DisplayOrder:
    out: DisplayOrder = {}  # type: ignore[typeddict-item]
    if "contents" in data:
        import aws_sdk_apigatewayv2.types.__list_of_section

        out["contents"] = aws_sdk_apigatewayv2.types.__list_of_section.deserialize_json(
            data["contents"]
        )
    if "overviewPageArn" in data:
        out["overview_page_arn"] = data["overviewPageArn"]
    if "productPageArns" in data:
        import aws_sdk_apigatewayv2.types.__list_of__string_min20_max2048

        out["product_page_arns"] = (
            aws_sdk_apigatewayv2.types.__list_of__string_min20_max2048.deserialize_json(
                data["productPageArns"]
            )
        )
    return out
