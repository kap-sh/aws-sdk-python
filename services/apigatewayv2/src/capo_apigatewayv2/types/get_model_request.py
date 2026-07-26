"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#GetModelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__string


class GetModelRequest(TypedDict, closed=True):
    api_id: "capo_apigatewayv2.types.__string.__string"
    """<p>The API identifier.</p>"""
    model_id: "capo_apigatewayv2.types.__string.__string"
    """<p>The model ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetModelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetModelRequest:
    out: GetModelRequest = {}  # type: ignore[typeddict-item]
    return out
