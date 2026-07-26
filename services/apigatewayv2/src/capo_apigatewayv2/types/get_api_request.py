"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#GetApiRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__string


class GetApiRequest(TypedDict, closed=True):
    api_id: "capo_apigatewayv2.types.__string.__string"
    """<p>The API identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetApiRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetApiRequest:
    out: GetApiRequest = {}  # type: ignore[typeddict-item]
    return out
