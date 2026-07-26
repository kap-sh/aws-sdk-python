"""Generated from Smithy shape ``com.amazonaws.apigateway#DeleteResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.string


class DeleteResourceRequest(TypedDict, closed=True):
    rest_api_id: "capo_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    resource_id: "capo_api_gateway.types.string.String"
    """<p>The identifier of the Resource resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteResourceRequest:
    out: DeleteResourceRequest = {}  # type: ignore[typeddict-item]
    return out
