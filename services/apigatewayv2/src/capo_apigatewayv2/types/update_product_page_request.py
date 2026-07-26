"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#UpdateProductPageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__string
    import capo_apigatewayv2.types.display_content


class UpdateProductPageRequest(TypedDict, closed=True):
    display_content: NotRequired[
        "capo_apigatewayv2.types.display_content.DisplayContent"
    ]
    """<p>The content of the product page.</p>"""
    portal_product_id: "capo_apigatewayv2.types.__string.__string"
    """<p>The portal product identifier.</p>"""
    product_page_id: "capo_apigatewayv2.types.__string.__string"
    """<p>The portal product identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateProductPageRequest) -> dict:
    out: dict = {}
    if "display_content" in value:
        import capo_apigatewayv2.types.display_content

        out["displayContent"] = capo_apigatewayv2.types.display_content.serialize_json(
            value["display_content"]
        )
    return out


def deserialize_json(data: dict) -> UpdateProductPageRequest:
    out: UpdateProductPageRequest = {}  # type: ignore[typeddict-item]
    if "displayContent" in data:
        import capo_apigatewayv2.types.display_content

        out["display_content"] = (
            capo_apigatewayv2.types.display_content.deserialize_json(
                data["displayContent"]
            )
        )
    return out
