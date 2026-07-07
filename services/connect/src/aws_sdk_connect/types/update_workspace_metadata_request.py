"""Generated from Smithy shape ``com.amazonaws.connect#UpdateWorkspaceMetadataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.workspace_description
    import aws_sdk_connect.types.workspace_id
    import aws_sdk_connect.types.workspace_name
    import aws_sdk_connect.types.workspace_title


class UpdateWorkspaceMetadataRequest(TypedDict, closed=True):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    workspace_id: "aws_sdk_connect.types.workspace_id.WorkspaceId"
    """<p>The identifier of the workspace.</p>"""
    name: NotRequired["aws_sdk_connect.types.workspace_name.WorkspaceName"]
    """<p>The name of the workspace.</p>"""
    description: NotRequired[
        "aws_sdk_connect.types.workspace_description.WorkspaceDescription"
    ]
    """<p>The description of the workspace.</p>"""
    title: NotRequired["aws_sdk_connect.types.workspace_title.WorkspaceTitle"]
    """<p>The title displayed for the workspace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWorkspaceMetadataRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "title" in value:
        out["Title"] = value["title"]
    return out


def deserialize_json(data: dict) -> UpdateWorkspaceMetadataRequest:
    out: UpdateWorkspaceMetadataRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Title" in data:
        out["title"] = data["Title"]
    return out
