"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#GetModelTemplateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string


class GetModelTemplateResponse(TypedDict):
    value: NotRequired["aws_sdk_apigatewayv2.types.__string.__string"]
    """<p>The template value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetModelTemplateResponse) -> dict:
    out: dict = {}
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> GetModelTemplateResponse:
    out: GetModelTemplateResponse = {}  # type: ignore[typeddict-item]
    if "value" in data:
        out["value"] = data["value"]
    return out
