"""Generated from Smithy shape ``com.amazonaws.appsync#DeleteApiKeyRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appsync.types.string


class DeleteApiKeyRequest(TypedDict):
    api_id: "aws_sdk_appsync.types.string.String"
    """<p>The API ID.</p>"""
    id: "aws_sdk_appsync.types.string.String"
    """<p>The ID for the API key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteApiKeyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteApiKeyRequest:
    out: DeleteApiKeyRequest = {}  # type: ignore[typeddict-item]
    return out
