"""Generated from Smithy shape ``com.amazonaws.apigateway#GetModelTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.string


class GetModelTemplateRequest(TypedDict, closed=True):
    rest_api_id: "capo_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    model_name: "capo_api_gateway.types.string.String"
    """<p>The name of the model for which to generate a template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetModelTemplateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetModelTemplateRequest:
    out: GetModelTemplateRequest = {}  # type: ignore[typeddict-item]
    return out
