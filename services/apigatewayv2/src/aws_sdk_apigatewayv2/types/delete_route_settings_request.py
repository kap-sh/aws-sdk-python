"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#DeleteRouteSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string


class DeleteRouteSettingsRequest(TypedDict, closed=True):
    api_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The API identifier.</p>"""
    route_key: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The route key.</p>"""
    stage_name: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The stage name. Stage names can only contain alphanumeric characters, hyphens, and underscores. Maximum length is 128 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRouteSettingsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRouteSettingsRequest:
    out: DeleteRouteSettingsRequest = {}  # type: ignore[typeddict-item]
    return out
