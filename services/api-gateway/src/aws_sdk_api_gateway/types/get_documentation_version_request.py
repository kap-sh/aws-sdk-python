"""Generated from Smithy shape ``com.amazonaws.apigateway#GetDocumentationVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.string


class GetDocumentationVersionRequest(TypedDict, closed=True):
    rest_api_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    documentation_version: "aws_sdk_api_gateway.types.string.String"
    """<p>The version identifier of the to-be-retrieved documentation snapshot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDocumentationVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDocumentationVersionRequest:
    out: GetDocumentationVersionRequest = {}  # type: ignore[typeddict-item]
    return out
