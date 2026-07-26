"""Generated from Smithy shape ``com.amazonaws.apigateway#DeleteRestApiRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.string


class DeleteRestApiRequest(TypedDict, closed=True):
    rest_api_id: "capo_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRestApiRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRestApiRequest:
    out: DeleteRestApiRequest = {}  # type: ignore[typeddict-item]
    return out
