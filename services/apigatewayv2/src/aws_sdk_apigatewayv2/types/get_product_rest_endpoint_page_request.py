"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#GetProductRestEndpointPageRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string


class GetProductRestEndpointPageRequest(TypedDict):
    include_raw_display_content: NotRequired[
        "aws_sdk_apigatewayv2.types.__string.__string"
    ]
    """<p>The query parameter to include raw display content.</p>"""
    portal_product_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The portal product identifier.</p>"""
    product_rest_endpoint_page_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The product REST endpoint identifier.</p>"""
    resource_owner_account_id: NotRequired[
        "aws_sdk_apigatewayv2.types.__string.__string"
    ]
    """<p>The account ID of the resource owner of the portal product.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProductRestEndpointPageRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetProductRestEndpointPageRequest:
    out: GetProductRestEndpointPageRequest = {}  # type: ignore[typeddict-item]
    return out
