"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#CreateProductPageRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string
    import aws_sdk_apigatewayv2.types.display_content


class CreateProductPageRequest(TypedDict):
    display_content: NotRequired[
        "aws_sdk_apigatewayv2.types.display_content.DisplayContent"
    ]
    """<p>The content of the product page.</p>"""
    portal_product_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The portal product identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProductPageRequest) -> dict:
    out: dict = {}
    if "display_content" in value:
        import aws_sdk_apigatewayv2.types.display_content

        out["displayContent"] = (
            aws_sdk_apigatewayv2.types.display_content.serialize_json(
                value["display_content"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateProductPageRequest:
    out: CreateProductPageRequest = {}  # type: ignore[typeddict-item]
    if "displayContent" in data:
        import aws_sdk_apigatewayv2.types.display_content

        out["display_content"] = (
            aws_sdk_apigatewayv2.types.display_content.deserialize_json(
                data["displayContent"]
            )
        )
    return out
