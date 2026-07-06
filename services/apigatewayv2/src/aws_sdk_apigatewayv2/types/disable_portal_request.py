"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#DisablePortalRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string


class DisablePortalRequest(TypedDict, closed=True):
    portal_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The portal identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisablePortalRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisablePortalRequest:
    out: DisablePortalRequest = {}  # type: ignore[typeddict-item]
    return out
