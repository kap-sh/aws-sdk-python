"""Generated from Smithy shape ``com.amazonaws.appsync#DeleteApiKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.string


class DeleteApiKeyRequest(TypedDict, closed=True):
    api_id: "capo_appsync.types.string.String"
    """<p>The API ID.</p>"""
    id: "capo_appsync.types.string.String"
    """<p>The ID for the API key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteApiKeyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteApiKeyRequest:
    out: DeleteApiKeyRequest = {}  # type: ignore[typeddict-item]
    return out
