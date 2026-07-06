"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#GetModelTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string


class GetModelTemplateRequest(TypedDict, closed=True):
    api_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The API identifier.</p>"""
    model_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The model ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetModelTemplateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetModelTemplateRequest:
    out: GetModelTemplateRequest = {}  # type: ignore[typeddict-item]
    return out
