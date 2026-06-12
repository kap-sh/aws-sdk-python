"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#GetProductPageRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string


class GetProductPageRequest(TypedDict):
    portal_product_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The portal product identifier.</p>"""
    product_page_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The portal product identifier.</p>"""
    resource_owner_account_id: NotRequired[
        "aws_sdk_apigatewayv2.types.__string.__string"
    ]
    """<p>The account ID of the resource owner of the portal product.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProductPageRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetProductPageRequest:
    out: GetProductPageRequest = {}  # type: ignore[typeddict-item]
    return out
