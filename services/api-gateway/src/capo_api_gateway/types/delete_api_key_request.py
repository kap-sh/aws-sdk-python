"""Generated from Smithy shape ``com.amazonaws.apigateway#DeleteApiKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.string


class DeleteApiKeyRequest(TypedDict, closed=True):
    api_key: "capo_api_gateway.types.string.String"
    """<p>The identifier of the ApiKey resource to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteApiKeyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteApiKeyRequest:
    out: DeleteApiKeyRequest = {}  # type: ignore[typeddict-item]
    return out
