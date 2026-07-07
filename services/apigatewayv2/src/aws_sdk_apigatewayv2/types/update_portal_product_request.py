"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#UpdatePortalProductRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string
    import aws_sdk_apigatewayv2.types.__string_min0_max1024
    import aws_sdk_apigatewayv2.types.__string_min1_max255
    import aws_sdk_apigatewayv2.types.display_order


class UpdatePortalProductRequest(TypedDict, closed=True):
    description: NotRequired[
        "aws_sdk_apigatewayv2.types.__string_min0_max1024.__stringMin0Max1024"
    ]
    """<p>The description.</p>"""
    display_name: NotRequired[
        "aws_sdk_apigatewayv2.types.__string_min1_max255.__stringMin1Max255"
    ]
    """<p>The displayName.</p>"""
    display_order: NotRequired["aws_sdk_apigatewayv2.types.display_order.DisplayOrder"]
    """<p>The display order.</p>"""
    portal_product_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The portal product identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePortalProductRequest) -> dict:
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
    return out


def deserialize_json(data: dict) -> UpdatePortalProductRequest:
    out: UpdatePortalProductRequest = {}  # type: ignore[typeddict-item]
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
    return out
