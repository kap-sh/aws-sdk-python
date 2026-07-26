"""Generated from Smithy shape ``com.amazonaws.apigateway#DeleteDocumentationPartRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.string


class DeleteDocumentationPartRequest(TypedDict, closed=True):
    rest_api_id: "capo_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    documentation_part_id: "capo_api_gateway.types.string.String"
    """<p>The identifier of the to-be-deleted documentation part.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDocumentationPartRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDocumentationPartRequest:
    out: DeleteDocumentationPartRequest = {}  # type: ignore[typeddict-item]
    return out
