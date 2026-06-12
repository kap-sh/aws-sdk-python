"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#GetModelRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string


class GetModelRequest(TypedDict):
    api_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The API identifier.</p>"""
    model_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The model ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetModelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetModelRequest:
    out: GetModelRequest = {}  # type: ignore[typeddict-item]
    return out
