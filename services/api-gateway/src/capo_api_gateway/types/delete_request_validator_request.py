"""Generated from Smithy shape ``com.amazonaws.apigateway#DeleteRequestValidatorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.string


class DeleteRequestValidatorRequest(TypedDict, closed=True):
    rest_api_id: "capo_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    request_validator_id: "capo_api_gateway.types.string.String"
    """<p>The identifier of the RequestValidator to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRequestValidatorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRequestValidatorRequest:
    out: DeleteRequestValidatorRequest = {}  # type: ignore[typeddict-item]
    return out
