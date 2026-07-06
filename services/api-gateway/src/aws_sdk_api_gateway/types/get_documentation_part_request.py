"""Generated from Smithy shape ``com.amazonaws.apigateway#GetDocumentationPartRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.string


class GetDocumentationPartRequest(TypedDict, closed=True):
    rest_api_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    documentation_part_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDocumentationPartRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDocumentationPartRequest:
    out: GetDocumentationPartRequest = {}  # type: ignore[typeddict-item]
    return out
