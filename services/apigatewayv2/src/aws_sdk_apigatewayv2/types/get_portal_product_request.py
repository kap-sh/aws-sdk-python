"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#GetPortalProductRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string


class GetPortalProductRequest(TypedDict, closed=True):
    portal_product_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The portal product identifier.</p>"""
    resource_owner_account_id: NotRequired[
        "aws_sdk_apigatewayv2.types.__string.__string"
    ]
    """<p>The account ID of the resource owner of the portal product.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPortalProductRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPortalProductRequest:
    out: GetPortalProductRequest = {}  # type: ignore[typeddict-item]
    return out
