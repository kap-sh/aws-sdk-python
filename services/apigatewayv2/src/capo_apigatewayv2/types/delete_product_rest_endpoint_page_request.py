"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#DeleteProductRestEndpointPageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__string


class DeleteProductRestEndpointPageRequest(TypedDict, closed=True):
    portal_product_id: "capo_apigatewayv2.types.__string.__string"
    """<p>The portal product identifier.</p>"""
    product_rest_endpoint_page_id: "capo_apigatewayv2.types.__string.__string"
    """<p>The product REST endpoint identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteProductRestEndpointPageRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteProductRestEndpointPageRequest:
    out: DeleteProductRestEndpointPageRequest = {}  # type: ignore[typeddict-item]
    return out
