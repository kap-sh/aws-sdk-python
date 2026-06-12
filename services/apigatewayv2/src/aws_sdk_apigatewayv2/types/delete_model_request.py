"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#DeleteModelRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string


class DeleteModelRequest(TypedDict):
    api_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The API identifier.</p>"""
    model_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The model ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteModelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteModelRequest:
    out: DeleteModelRequest = {}  # type: ignore[typeddict-item]
    return out
