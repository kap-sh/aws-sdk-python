"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#DeletePortalProductSharingPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__string


class DeletePortalProductSharingPolicyRequest(TypedDict, closed=True):
    portal_product_id: "capo_apigatewayv2.types.__string.__string"
    """<p>The portal product identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePortalProductSharingPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePortalProductSharingPolicyRequest:
    out: DeletePortalProductSharingPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
