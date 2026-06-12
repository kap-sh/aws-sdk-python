"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#ListProductPagesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string


class ListProductPagesRequest(TypedDict):
    max_results: NotRequired["aws_sdk_apigatewayv2.types.__string.__string"]
    """<p>The maximum number of elements to be returned for this resource.</p>"""
    next_token: NotRequired["aws_sdk_apigatewayv2.types.__string.__string"]
    """<p>The next page of elements from this collection. Not valid for the last element of the collection.</p>"""
    portal_product_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The portal product identifier.</p>"""
    resource_owner_account_id: NotRequired[
        "aws_sdk_apigatewayv2.types.__string.__string"
    ]
    """<p>The account ID of the resource owner of the portal product.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProductPagesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListProductPagesRequest:
    out: ListProductPagesRequest = {}  # type: ignore[typeddict-item]
    return out
