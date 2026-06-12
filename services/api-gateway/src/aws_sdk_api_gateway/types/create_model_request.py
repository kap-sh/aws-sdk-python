"""Generated from Smithy shape ``com.amazonaws.apigateway#CreateModelRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_api_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.string


class CreateModelRequest(TypedDict):
    rest_api_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The RestApi identifier under which the Model will be created.</p>"""
    name: "aws_sdk_api_gateway.types.string.String"
    """<p>The name of the model. Must be alphanumeric.</p>"""
    description: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The description of the model.</p>"""
    schema: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The schema for the model. For <code>application/json</code> models, this should be JSON schema draft 4 model. The maximum size of the model is 400 KB.</p>"""
    content_type: "aws_sdk_api_gateway.types.string.String"
    """<p>The content-type for the model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateModelRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "schema" in value:
        out["schema"] = value["schema"]
    out["contentType"] = value["content_type"]
    return out


def deserialize_json(data: dict) -> CreateModelRequest:
    out: CreateModelRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateModelRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "schema" in data:
        out["schema"] = data["schema"]
    if "contentType" in data:
        out["content_type"] = data["contentType"]
    else:
        raise DeserializationError("CreateModelRequest.content_type required")
    return out
