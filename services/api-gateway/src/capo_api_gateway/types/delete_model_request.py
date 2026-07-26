"""Generated from Smithy shape ``com.amazonaws.apigateway#DeleteModelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.string


class DeleteModelRequest(TypedDict, closed=True):
    rest_api_id: "capo_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    model_name: "capo_api_gateway.types.string.String"
    """<p>The name of the model to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteModelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteModelRequest:
    out: DeleteModelRequest = {}  # type: ignore[typeddict-item]
    return out
