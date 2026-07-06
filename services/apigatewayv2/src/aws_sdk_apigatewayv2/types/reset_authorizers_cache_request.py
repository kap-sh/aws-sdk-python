"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#ResetAuthorizersCacheRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string


class ResetAuthorizersCacheRequest(TypedDict, closed=True):
    api_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The API identifier.</p>"""
    stage_name: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The stage name. Stage names can contain only alphanumeric characters, hyphens, and underscores, or be $default. Maximum length is 128 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResetAuthorizersCacheRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ResetAuthorizersCacheRequest:
    out: ResetAuthorizersCacheRequest = {}  # type: ignore[typeddict-item]
    return out
