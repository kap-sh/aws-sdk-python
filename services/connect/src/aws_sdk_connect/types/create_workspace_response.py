"""Generated from Smithy shape ``com.amazonaws.connect#CreateWorkspaceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.workspace_id


class CreateWorkspaceResponse(TypedDict):
    workspace_id: "aws_sdk_connect.types.workspace_id.WorkspaceId"
    """<p>The identifier of the workspace.</p>"""
    workspace_arn: "aws_sdk_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the workspace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkspaceResponse) -> dict:
    out: dict = {}
    out["WorkspaceId"] = value["workspace_id"]
    out["WorkspaceArn"] = value["workspace_arn"]
    return out


def deserialize_json(data: dict) -> CreateWorkspaceResponse:
    out: CreateWorkspaceResponse = {}  # type: ignore[typeddict-item]
    if "WorkspaceId" in data:
        out["workspace_id"] = data["WorkspaceId"]
    else:
        raise DeserializationError("CreateWorkspaceResponse.workspace_id required")
    if "WorkspaceArn" in data:
        out["workspace_arn"] = data["WorkspaceArn"]
    else:
        raise DeserializationError("CreateWorkspaceResponse.workspace_arn required")
    return out
