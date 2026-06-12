"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#DeletePortalProductRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string


class DeletePortalProductRequest(TypedDict):
    portal_product_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The portal product identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePortalProductRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePortalProductRequest:
    out: DeletePortalProductRequest = {}  # type: ignore[typeddict-item]
    return out
