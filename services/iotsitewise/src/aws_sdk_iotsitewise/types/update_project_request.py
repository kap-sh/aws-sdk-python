"""Generated from Smithy shape ``com.amazonaws.iotsitewise#UpdateProjectRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.client_token
    import aws_sdk_iotsitewise.types.description
    import aws_sdk_iotsitewise.types.id
    import aws_sdk_iotsitewise.types.name


class UpdateProjectRequest(TypedDict):
    project_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the project to update.</p>"""
    project_name: "aws_sdk_iotsitewise.types.name.Name"
    """<p>A new friendly name for the project.</p>"""
    project_description: NotRequired[
        "aws_sdk_iotsitewise.types.description.Description"
    ]
    """<p>A new description for the project.</p>"""
    client_token: NotRequired["aws_sdk_iotsitewise.types.client_token.ClientToken"]
    """<p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateProjectRequest) -> dict:
    out: dict = {}
    out["projectName"] = value["project_name"]
    if "project_description" in value:
        out["projectDescription"] = value["project_description"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateProjectRequest:
    out: UpdateProjectRequest = {}  # type: ignore[typeddict-item]
    if "projectName" in data:
        out["project_name"] = data["projectName"]
    else:
        raise DeserializationError("UpdateProjectRequest.project_name required")
    if "projectDescription" in data:
        out["project_description"] = data["projectDescription"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
