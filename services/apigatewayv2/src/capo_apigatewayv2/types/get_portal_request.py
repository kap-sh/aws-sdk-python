"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#GetPortalRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__string


class GetPortalRequest(TypedDict, closed=True):
    portal_id: "capo_apigatewayv2.types.__string.__string"
    """<p>The portal identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPortalRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPortalRequest:
    out: GetPortalRequest = {}  # type: ignore[typeddict-item]
    return out
