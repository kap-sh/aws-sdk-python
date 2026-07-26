"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#GetStageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__string


class GetStageRequest(TypedDict, closed=True):
    api_id: "capo_apigatewayv2.types.__string.__string"
    """<p>The API identifier.</p>"""
    stage_name: "capo_apigatewayv2.types.__string.__string"
    """<p>The stage name. Stage names can only contain alphanumeric characters, hyphens, and underscores. Maximum length is 128 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetStageRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetStageRequest:
    out: GetStageRequest = {}  # type: ignore[typeddict-item]
    return out
