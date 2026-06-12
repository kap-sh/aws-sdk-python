"""Generated from Smithy shape ``com.amazonaws.apigateway#GetModelTemplateRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.string


class GetModelTemplateRequest(TypedDict):
    rest_api_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    model_name: "aws_sdk_api_gateway.types.string.String"
    """<p>The name of the model for which to generate a template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetModelTemplateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetModelTemplateRequest:
    out: GetModelTemplateRequest = {}  # type: ignore[typeddict-item]
    return out
