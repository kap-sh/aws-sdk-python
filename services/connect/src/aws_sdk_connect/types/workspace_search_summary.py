"""Generated from Smithy shape ``com.amazonaws.connect#WorkspaceSearchSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.tag_map
    import aws_sdk_connect.types.timestamp
    import aws_sdk_connect.types.visibility
    import aws_sdk_connect.types.workspace_description
    import aws_sdk_connect.types.workspace_id
    import aws_sdk_connect.types.workspace_name
    import aws_sdk_connect.types.workspace_title


class WorkspaceSearchSummary(TypedDict):
    id: NotRequired["aws_sdk_connect.types.workspace_id.WorkspaceId"]
    """<p>The unique identifier of the workspace.</p>"""
    name: NotRequired["aws_sdk_connect.types.workspace_name.WorkspaceName"]
    """<p>The name of the workspace.</p>"""
    visibility: NotRequired["aws_sdk_connect.types.visibility.Visibility"]
    """<p>The visibility setting of the workspace.</p>"""
    description: NotRequired[
        "aws_sdk_connect.types.workspace_description.WorkspaceDescription"
    ]
    """<p>The description of the workspace.</p>"""
    title: NotRequired["aws_sdk_connect.types.workspace_title.WorkspaceTitle"]
    """<p>The title displayed for the workspace.</p>"""
    arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the workspace.</p>"""
    created_at: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when the workspace was created.</p>"""
    tags: NotRequired["aws_sdk_connect.types.tag_map.TagMap"]
    """<p>The tags associated with the workspace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkspaceSearchSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "visibility" in value:
        import aws_sdk_connect.types.visibility

        out["Visibility"] = aws_sdk_connect.types.visibility.serialize_json(
            value["visibility"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "title" in value:
        out["Title"] = value["title"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "created_at" in value:
        import aws_sdk_connect.types.timestamp

        out["CreatedAt"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "tags" in value:
        import aws_sdk_connect.types.tag_map

        out["Tags"] = aws_sdk_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> WorkspaceSearchSummary:
    out: WorkspaceSearchSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Visibility" in data:
        import aws_sdk_connect.types.visibility

        out["visibility"] = aws_sdk_connect.types.visibility.deserialize_json(
            data["Visibility"]
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "Title" in data:
        out["title"] = data["Title"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "CreatedAt" in data:
        import aws_sdk_connect.types.timestamp

        out["created_at"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    if "Tags" in data:
        import aws_sdk_connect.types.tag_map

        out["tags"] = aws_sdk_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
