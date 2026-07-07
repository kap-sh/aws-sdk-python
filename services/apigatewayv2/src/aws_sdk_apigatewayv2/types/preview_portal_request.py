"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#PreviewPortalRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string


class PreviewPortalRequest(TypedDict, closed=True):
    portal_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The portal identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PreviewPortalRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> PreviewPortalRequest:
    out: PreviewPortalRequest = {}  # type: ignore[typeddict-item]
    return out
