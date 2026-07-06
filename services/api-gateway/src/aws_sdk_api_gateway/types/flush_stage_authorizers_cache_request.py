"""Generated from Smithy shape ``com.amazonaws.apigateway#FlushStageAuthorizersCacheRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.string


class FlushStageAuthorizersCacheRequest(TypedDict, closed=True):
    rest_api_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    stage_name: "aws_sdk_api_gateway.types.string.String"
    """<p>The name of the stage to flush.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlushStageAuthorizersCacheRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> FlushStageAuthorizersCacheRequest:
    out: FlushStageAuthorizersCacheRequest = {}  # type: ignore[typeddict-item]
    return out
