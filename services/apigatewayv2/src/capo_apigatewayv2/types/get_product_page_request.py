"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#GetProductPageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__string


class GetProductPageRequest(TypedDict, closed=True):
    portal_product_id: "capo_apigatewayv2.types.__string.__string"
    """<p>The portal product identifier.</p>"""
    product_page_id: "capo_apigatewayv2.types.__string.__string"
    """<p>The portal product identifier.</p>"""
    resource_owner_account_id: NotRequired["capo_apigatewayv2.types.__string.__string"]
    """<p>The account ID of the resource owner of the portal product.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProductPageRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetProductPageRequest:
    out: GetProductPageRequest = {}  # type: ignore[typeddict-item]
    return out
