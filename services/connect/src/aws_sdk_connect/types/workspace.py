"""Generated from Smithy shape ``com.amazonaws.connect#Workspace``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.region_name
    import aws_sdk_connect.types.tag_map
    import aws_sdk_connect.types.timestamp
    import aws_sdk_connect.types.visibility
    import aws_sdk_connect.types.workspace_description
    import aws_sdk_connect.types.workspace_id
    import aws_sdk_connect.types.workspace_name
    import aws_sdk_connect.types.workspace_theme
    import aws_sdk_connect.types.workspace_title


class Workspace(TypedDict, closed=True):
    visibility: NotRequired["aws_sdk_connect.types.visibility.Visibility"]
    """<p>Controls who can access the workspace. Valid values are: <code>ALL</code> (all users), <code>ASSIGNED</code> (only assigned users and routing profiles), and <code>NONE</code> (not visible).</p>"""
    id: "aws_sdk_connect.types.workspace_id.WorkspaceId"
    """<p>The unique identifier of the workspace.</p>"""
    name: "aws_sdk_connect.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace.</p>"""
    arn: "aws_sdk_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the workspace.</p>"""
    description: NotRequired[
        "aws_sdk_connect.types.workspace_description.WorkspaceDescription"
    ]
    """<p>The description of the workspace.</p>"""
    theme: NotRequired["aws_sdk_connect.types.workspace_theme.WorkspaceTheme"]
    """<p>The theme configuration for the workspace, including colors and styling.</p>"""
    title: NotRequired["aws_sdk_connect.types.workspace_title.WorkspaceTitle"]
    """<p>The title displayed for the workspace.</p>"""
    last_modified_time: "aws_sdk_connect.types.timestamp.Timestamp"
    """<p>The timestamp when the workspace was last modified.</p>"""
    last_modified_region: NotRequired["aws_sdk_connect.types.region_name.RegionName"]
    """<p>The Amazon Web Services Region where the workspace was last modified.</p>"""
    tags: NotRequired["aws_sdk_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for the workspace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Workspace) -> dict:
    out: dict = {}
    if "visibility" in value:
        import aws_sdk_connect.types.visibility

        out["Visibility"] = aws_sdk_connect.types.visibility.serialize_json(
            value["visibility"]
        )
    out["Id"] = value["id"]
    out["Name"] = value["name"]
    out["Arn"] = value["arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "theme" in value:
        import aws_sdk_connect.types.workspace_theme

        out["Theme"] = aws_sdk_connect.types.workspace_theme.serialize_json(
            value["theme"]
        )
    if "title" in value:
        out["Title"] = value["title"]
    import aws_sdk_connect.types.timestamp

    out["LastModifiedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
        value["last_modified_time"]
    )
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    if "tags" in value:
        import aws_sdk_connect.types.tag_map

        out["Tags"] = aws_sdk_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> Workspace:
    out: Workspace = {}  # type: ignore[typeddict-item]
    if "Visibility" in data:
        import aws_sdk_connect.types.visibility

        out["visibility"] = aws_sdk_connect.types.visibility.deserialize_json(
            data["Visibility"]
        )
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("Workspace.id required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("Workspace.name required")
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("Workspace.arn required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "Theme" in data:
        import aws_sdk_connect.types.workspace_theme

        out["theme"] = aws_sdk_connect.types.workspace_theme.deserialize_json(
            data["Theme"]
        )
    if "Title" in data:
        out["title"] = data["Title"]
    if "LastModifiedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["last_modified_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    else:
        raise DeserializationError("Workspace.last_modified_time required")
    if "LastModifiedRegion" in data:
        out["last_modified_region"] = data["LastModifiedRegion"]
    if "Tags" in data:
        import aws_sdk_connect.types.tag_map

        out["tags"] = aws_sdk_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
