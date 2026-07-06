"""Generated from Smithy shape ``com.amazonaws.apigateway#CreateResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_api_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.string


class CreateResourceRequest(TypedDict, closed=True):
    rest_api_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    parent_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The parent resource's identifier.</p>"""
    path_part: "aws_sdk_api_gateway.types.string.String"
    """<p>The last path segment for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateResourceRequest) -> dict:
    out: dict = {}
    out["pathPart"] = value["path_part"]
    return out


def deserialize_json(data: dict) -> CreateResourceRequest:
    out: CreateResourceRequest = {}  # type: ignore[typeddict-item]
    if "pathPart" in data:
        out["path_part"] = data["pathPart"]
    else:
        raise DeserializationError("CreateResourceRequest.path_part required")
    return out
