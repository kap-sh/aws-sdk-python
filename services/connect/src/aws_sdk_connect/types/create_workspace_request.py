"""Generated from Smithy shape ``com.amazonaws.connect#CreateWorkspaceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.tag_map
    import aws_sdk_connect.types.workspace_description
    import aws_sdk_connect.types.workspace_name
    import aws_sdk_connect.types.workspace_theme
    import aws_sdk_connect.types.workspace_title


class CreateWorkspaceRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    name: "aws_sdk_connect.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace. Must be unique within the instance and can contain 1-127 characters.</p>"""
    description: NotRequired[
        "aws_sdk_connect.types.workspace_description.WorkspaceDescription"
    ]
    """<p>The description of the workspace. Maximum length is 250 characters.</p>"""
    theme: NotRequired["aws_sdk_connect.types.workspace_theme.WorkspaceTheme"]
    """<p>The theme configuration for the workspace, including colors and styling.</p>"""
    title: NotRequired["aws_sdk_connect.types.workspace_title.WorkspaceTitle"]
    """<p>The title displayed for the workspace.</p>"""
    tags: NotRequired["aws_sdk_connect.types.tag_map.TagMap"]
    r"""<p>The tags used to organize, track, or control access for this resource. For example, <code>{ \"Tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkspaceRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "theme" in value:
        import aws_sdk_connect.types.workspace_theme

        out["Theme"] = aws_sdk_connect.types.workspace_theme.serialize_json(
            value["theme"]
        )
    if "title" in value:
        out["Title"] = value["title"]
    if "tags" in value:
        import aws_sdk_connect.types.tag_map

        out["Tags"] = aws_sdk_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateWorkspaceRequest:
    out: CreateWorkspaceRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateWorkspaceRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "Theme" in data:
        import aws_sdk_connect.types.workspace_theme

        out["theme"] = aws_sdk_connect.types.workspace_theme.deserialize_json(
            data["Theme"]
        )
    if "Title" in data:
        out["title"] = data["Title"]
    if "Tags" in data:
        import aws_sdk_connect.types.tag_map

        out["tags"] = aws_sdk_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
