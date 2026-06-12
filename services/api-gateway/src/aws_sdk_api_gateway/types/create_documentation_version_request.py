"""Generated from Smithy shape ``com.amazonaws.apigateway#CreateDocumentationVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_api_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.string


class CreateDocumentationVersionRequest(TypedDict):
    rest_api_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    documentation_version: "aws_sdk_api_gateway.types.string.String"
    """<p>The version identifier of the new snapshot.</p>"""
    stage_name: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The stage name to be associated with the new documentation snapshot.</p>"""
    description: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>A description about the new documentation snapshot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDocumentationVersionRequest) -> dict:
    out: dict = {}
    out["documentationVersion"] = value["documentation_version"]
    if "stage_name" in value:
        out["stageName"] = value["stage_name"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> CreateDocumentationVersionRequest:
    out: CreateDocumentationVersionRequest = {}  # type: ignore[typeddict-item]
    if "documentationVersion" in data:
        out["documentation_version"] = data["documentationVersion"]
    else:
        raise DeserializationError(
            "CreateDocumentationVersionRequest.documentation_version required"
        )
    if "stageName" in data:
        out["stage_name"] = data["stageName"]
    if "description" in data:
        out["description"] = data["description"]
    return out
