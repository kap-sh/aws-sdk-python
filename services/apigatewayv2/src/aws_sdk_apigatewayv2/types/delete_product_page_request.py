"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#DeleteProductPageRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string


class DeleteProductPageRequest(TypedDict):
    portal_product_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The portal product identifier.</p>"""
    product_page_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The portal product identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteProductPageRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteProductPageRequest:
    out: DeleteProductPageRequest = {}  # type: ignore[typeddict-item]
    return out
