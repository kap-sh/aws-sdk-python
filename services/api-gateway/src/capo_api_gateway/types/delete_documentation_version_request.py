"""Generated from Smithy shape ``com.amazonaws.apigateway#DeleteDocumentationVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.string


class DeleteDocumentationVersionRequest(TypedDict, closed=True):
    rest_api_id: "capo_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    documentation_version: "capo_api_gateway.types.string.String"
    """<p>The version identifier of a to-be-deleted documentation snapshot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDocumentationVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDocumentationVersionRequest:
    out: DeleteDocumentationVersionRequest = {}  # type: ignore[typeddict-item]
    return out
