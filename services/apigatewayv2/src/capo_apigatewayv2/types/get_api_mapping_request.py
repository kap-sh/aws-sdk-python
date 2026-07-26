"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#GetApiMappingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__string


class GetApiMappingRequest(TypedDict, closed=True):
    api_mapping_id: "capo_apigatewayv2.types.__string.__string"
    """<p>The API mapping identifier.</p>"""
    domain_name: "capo_apigatewayv2.types.__string.__string"
    """<p>The domain name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetApiMappingRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetApiMappingRequest:
    out: GetApiMappingRequest = {}  # type: ignore[typeddict-item]
    return out
