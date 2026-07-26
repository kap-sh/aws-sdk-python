"""Generated from Smithy shape ``com.amazonaws.apigateway#GetStageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.string


class GetStageRequest(TypedDict, closed=True):
    rest_api_id: "capo_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    stage_name: "capo_api_gateway.types.string.String"
    """<p>The name of the Stage resource to get information about.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetStageRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetStageRequest:
    out: GetStageRequest = {}  # type: ignore[typeddict-item]
    return out
