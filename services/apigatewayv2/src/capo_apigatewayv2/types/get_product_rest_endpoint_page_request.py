"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#GetProductRestEndpointPageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__string


class GetProductRestEndpointPageRequest(TypedDict, closed=True):
    include_raw_display_content: NotRequired[
        "capo_apigatewayv2.types.__string.__string"
    ]
    """<p>The query parameter to include raw display content.</p>"""
    portal_product_id: "capo_apigatewayv2.types.__string.__string"
    """<p>The portal product identifier.</p>"""
    product_rest_endpoint_page_id: "capo_apigatewayv2.types.__string.__string"
    """<p>The product REST endpoint identifier.</p>"""
    resource_owner_account_id: NotRequired["capo_apigatewayv2.types.__string.__string"]
    """<p>The account ID of the resource owner of the portal product.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProductRestEndpointPageRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetProductRestEndpointPageRequest:
    out: GetProductRestEndpointPageRequest = {}  # type: ignore[typeddict-item]
    return out
