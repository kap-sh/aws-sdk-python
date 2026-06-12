"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#GetPortalProductResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string_min0_max1024
    import aws_sdk_apigatewayv2.types.__string_min10_max30_pattern_az09
    import aws_sdk_apigatewayv2.types.__string_min1_max255
    import aws_sdk_apigatewayv2.types.__string_min20_max2048
    import aws_sdk_apigatewayv2.types.__timestamp_iso8601
    import aws_sdk_apigatewayv2.types.display_order
    import aws_sdk_apigatewayv2.types.tags


class GetPortalProductResponse(TypedDict):
    description: NotRequired[
        "aws_sdk_apigatewayv2.types.__string_min0_max1024.__stringMin0Max1024"
    ]
    """<p>The description of a portal product.</p>"""
    display_name: NotRequired[
        "aws_sdk_apigatewayv2.types.__string_min1_max255.__stringMin1Max255"
    ]
    """<p>The display name.</p>"""
    display_order: NotRequired["aws_sdk_apigatewayv2.types.display_order.DisplayOrder"]
    """<p>The display order.</p>"""
    last_modified: NotRequired[
        "aws_sdk_apigatewayv2.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The timestamp when the portal product was last modified.</p>"""
    portal_product_arn: NotRequired[
        "aws_sdk_apigatewayv2.types.__string_min20_max2048.__stringMin20Max2048"
    ]
    """<p>The ARN of the portal product.</p>"""
    portal_product_id: NotRequired[
        "aws_sdk_apigatewayv2.types.__string_min10_max30_pattern_az09.__stringMin10Max30PatternAZ09"
    ]
    """<p>The portal product identifier.</p>"""
    tags: NotRequired["aws_sdk_apigatewayv2.types.tags.Tags"]
    """<p>The collection of tags. Each tag element is associated with a given resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPortalProductResponse) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "display_order" in value:
        import aws_sdk_apigatewayv2.types.display_order

        out["displayOrder"] = aws_sdk_apigatewayv2.types.display_order.serialize_json(
            value["display_order"]
        )
    if "last_modified" in value:
        import aws_sdk_apigatewayv2.types.__timestamp_iso8601

        out["lastModified"] = (
            aws_sdk_apigatewayv2.types.__timestamp_iso8601.serialize_json(
                value["last_modified"]
            )
        )
    if "portal_product_arn" in value:
        out["portalProductArn"] = value["portal_product_arn"]
    if "portal_product_id" in value:
        out["portalProductId"] = value["portal_product_id"]
    if "tags" in value:
        import aws_sdk_apigatewayv2.types.tags

        out["tags"] = aws_sdk_apigatewayv2.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetPortalProductResponse:
    out: GetPortalProductResponse = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "displayOrder" in data:
        import aws_sdk_apigatewayv2.types.display_order

        out["display_order"] = (
            aws_sdk_apigatewayv2.types.display_order.deserialize_json(
                data["displayOrder"]
            )
        )
    if "lastModified" in data:
        import aws_sdk_apigatewayv2.types.__timestamp_iso8601

        out["last_modified"] = (
            aws_sdk_apigatewayv2.types.__timestamp_iso8601.deserialize_json(
                data["lastModified"]
            )
        )
    if "portalProductArn" in data:
        out["portal_product_arn"] = data["portalProductArn"]
    if "portalProductId" in data:
        out["portal_product_id"] = data["portalProductId"]
    if "tags" in data:
        import aws_sdk_apigatewayv2.types.tags

        out["tags"] = aws_sdk_apigatewayv2.types.tags.deserialize_json(data["tags"])
    return out
