"""Generated from Smithy shape ``com.amazonaws.apigateway#DeleteResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.string


class DeleteResourceRequest(TypedDict):
    rest_api_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    resource_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The identifier of the Resource resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteResourceRequest:
    out: DeleteResourceRequest = {}  # type: ignore[typeddict-item]
    return out
